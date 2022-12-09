from pyinfra.operations import server, apt, files, git
from pyinfra.facts.hardware import Ipv4Addresses
from pyinfra import inventory

cloud_controller_ip = next(filter(lambda ip: ip.startswith('192'), list(inventory.get_host('cloudcontroller').get_fact(
    Ipv4Addresses).values())))

server.shell(
    name="echo hostname",
    commands=["hostname"]
)

apt.packages(
    name="ensure unzip top is installed",
    packages=["unzip", "net-tools"],
    update=False,
    _sudo=True,
)

git.repo(
    name="clone kube-prometheus",
    src="https://github.com/prometheus-operator/kube-prometheus.git",
    dest="kube-prometheus"
)

server.shell(
    name="deploy kube-prometheus (all-in-one monitoring)",
    commands=[
        "kubectl apply --server-side -f kube-prometheus/manifests/setup",
        "kubectl wait --for condition=Established --all CustomResourceDefinition --namespace=monitoring",
        "kubectl apply -f kube-prometheus/manifests/",
        "kubectl wait --for condition=Ready pods --namespace=monitoring -l app.kubernetes.io/component=grafana  --timeout=90s"
    ]
)

server.shell(
    name="enable k8 port command",
    commands=[
        "nohup kubectl port-forward -n openfaas svc/gateway 8080:8080 > /dev/null 2>&1 &",
        "nohup kubectl port-forward -n monitoring --address {} svc/grafana 3000:3000 > /dev/null 2>&1 &".format(
            cloud_controller_ip),
        "nohup kubectl port-forward -n monitoring --address {} svc/prometheus 9090:9090 > /dev/null 2>&1 &".format(
            cloud_controller_ip)
    ]
)

server.wait(
    name="wait for openfaas gateway port to be available",
    port=8080
)

server.shell(
    name="set access to faas cli command",
    commands=[
        "kubectl get secret -n openfaas basic-auth -o jsonpath=\"{.data.basic-auth-password}\" | base64 --decode | faas-cli login --username admin --password-stdin"]
)

server.shell(
    name="docker login command",
    commands=["docker login -u macko99vu -p ZLZ@HSBsa654ey6"]
)

server.shell(
    name="creating functions directory",
    commands=["mkdir -p functions && cd functions"]
)

server.shell(
    name="export function name prefix",
    commands=["export OPENFAAS_PREFIX=macko99vu"]
)

server.shell(
    name="pull the function images",
    commands=[
        "docker pull macko99vu/file-upload:latest",
        "docker pull macko99vu/fibonacci:latest",
        "docker pull macko99vu/matmul:latest"]
)

files.put(
    name="upload functions config yml",
    src="./all_functions.yml",
    dest="./functions/all_functions.yml",
    mode="775",
)

# deploy_images_result = server.shell(
#     name="deploy the functions to openfaas",
#     commands=[
#         "if [ $(faas-cli list | grep file | wc -l) -eq 1 ]; then echo 'already deployed'; else faas-cli deploy --image macko99vu/file-upload --name file; fi",
#         "if [ $(faas-cli list | grep fibonacci | wc -l) -eq 1 ]; then echo 'already deployed'; else faas-cli deploy --image macko99vu/fibonacci --name fibonacci; fi",
#         "if [ $(faas-cli list | grep matmul | wc -l) -eq 1 ]; then echo 'already deployed'; else faas-cli deploy --image macko99vu/matmul --name matmul; fi"]
# )

deploy_images_result = server.shell(
    name="deploy the functions to openfaas",
    commands=[
        "faas-cli deploy --yaml ./functions/all_functions.yml"]
)

pull_data_sets_result = server.shell(
    name="pull images from NASA telescope",
    commands=[
        "if [ -e hst_media_0017.zip ] ; then echo 'zip already downloaded'; else wget -q https://esahubble.org/media/archives/media/zip/hst_media_0017.zip; fi ",
        "if [ -e ./images ] ; then echo 'unzip done'; else unzip -qq hst_media_0017.zip -d tmp_dir; fi",
        "if [ -e ./images ] ; then echo 'images ready'; else mv tmp_dir/imagecollection/large/ ./images; fi",
        "if [ -e tmp_dir ] ; then rm -r tmp_dir/; fi"
    ]
)

files.put(
    name="upload file_runner python script",
    src="./file_runner.py",
    dest="file_runner.py",
    mode="775",
)

files.put(
    name="upload fibonacci_runner python script",
    src="./fibonacci_runner.py",
    dest="fibonacci_runner.py",
    mode="775",
)

files.put(
    name="upload matmul_runner python script",
    src="./matmul_runner.py",
    dest="matmul_runner.py",
    mode="775",
)

file_result = server.shell(
    name="run file-upload function",
    commands=[
        "python3 file_runner.py"
    ]
)

fib_result = server.shell(
    name="run fibonacci function",
    commands=[
        "python3 fibonacci_runner.py"
    ]
)

matmul_result = server.shell(
    name="run matmul function",
    commands=[
        "python3 matmul_runner.py"
    ]
)