controller_hostname = "192.168.132.2"
controller_user = "cloud_controller_ds2022-lab2-1"
controller_key = "/home/ds2022-lab2-1/.ssh/id_rsa_benchmark"

ssh_servers = [
    ('cloudcontroller', {'ssh_hostname': controller_hostname,
                         'ssh_user': controller_user,
                         'ssh_key': controller_key}),
]
