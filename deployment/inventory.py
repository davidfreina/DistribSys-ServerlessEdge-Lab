import os
import sys

user = os.environ["USER"]

if user == "ds2022-lab2-1":
    controller_hostname = "192.168.132.2"
elif user == "ds2022-lab2-2":
    controller_hostname = "192.168.137.2"
elif user == "ds2022-lab2-3":
    controller_hostname = "192.168.139.2"
else:
    sys.exit("User unknown. Please edit deployment/inventory.py and add you cloud controller ip address")

controller_user = "cloud_controller_{}".format(user)
controller_key = "/home/{}/.ssh/id_rsa_benchmark".format(user)

ssh_servers = [
    ('cloudcontroller', {'ssh_hostname': controller_hostname,
                         'ssh_user': controller_user,
                         'ssh_key': controller_key}),
]