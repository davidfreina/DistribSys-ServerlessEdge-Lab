# HOW TO
### Prerequisites
- [pyinfra](https://pyinfra.com/)

In order to deploy to the right `cloud_controller` we need some information of the user.
This information should be provided in the [inventory.py](deployment/inventory.py).
The user should add an additional ``elif`` statement with the respective username and IP informations.

Furthermore the user has to edit the configurations files for continuum ([cloud_conf.cfg](configurations/cloud_conf.cfg) and [edge_conf.cfg](configurations/edge_conf.cfg)).
The changes need to be made to the following keys:
- `base_path`
- `middleIP`

### Deploying the project

````bash
cd ./DistribSys-ServerlessEdge-Lab/deployment/
````

Due to the automation provided by `pyinfra` setting up the monitoring and running various tests is as easy as:

````bash
pyinfra inventory.py deploy.py
````

### Open Grafana on your localhost

To view the dashboards locally in your browser you need to forward port 3000 from the `cloud_controller` to your localhost.

We found the easiest way to do this is by configuring proxy jumping from your host to the respective node on the dss cluster.

You can find an example ssh-config and command down below which forwards port 3000 from node4 on the dss cluster directly to your local host.

````
Host dss-cluster
        Hostname <DSS_CLUSTER_HOSTNAME>
        User <DSS_CLUSTER_USERNAME>
        IdentityFile <PATH_TO_PRIVATE_KEY_DSS_CLUSTER>
        PreferredAuthentications publickey

Host dss-node
        Hostname <DSS_NODE_HOSTNAME>
        User <DSS_NODE_USERNAME>
        ProxyJump dss-cluster
        IdentityFile <PATH_TO_PRIVATE_KEY_DSS_NODE>
        PreferredAuthentications publickey
````

````bash
ssh -L 3000:<CLOUD_CONTROLLER_IP>:3000 -J dss-cluster dss-node
````