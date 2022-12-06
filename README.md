## HOW TO

`nohup kubectl port-forward -n openfaas svc/gateway 8080:8080 &`

`PASSWORD=$(kubectl get secret -n openfaas basic-auth -o jsonpath="{.data.basic-auth-password}" | base64 --decode; echo)`

`echo -n $PASSWORD | faas-cli login --username admin --password-stdin`

`python3 main.py configuration/config_test.cfg`

`ssh cloud_controller_ds2022-lab2-1@192.168.132.2 -i /home/ds2022-lab2-1/.ssh/id_rsa_benchmark`

`docker login`

`mkdir functions && cd functions`

`export OPENFAAS_PREFIX=macko99vu`

`docker pull macko99vu/file-upload:latest`

`faas-cli deploy --image macko99vu/file-upload --name file`

`curl http://127.0.0.1:8080/function/file -d 'abc'`

`curl -o img.jpg https://unsplash.com/photos/v3-zcCWMjgM/download?ixid=MnwxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNjY5ODM3NTI5&force=true&w=2400`

`curl -o result http://127.0.0.1:8080/function/file -d @img.jpg`