# Virtual Slurm

Slurm is a workload manager used in clusters and supercomputers.
For detailed documentaation on slurm please see:

* http://slurm.schedmd.com/

Virtual Slurm is a tool to help manage slurm deployment in cloudmesh
This project also includes installation of hadoop

## Commands

The following commands are added to cloudmesh on setting up this project
	slurm
	hadoop

The Slurm command gives the following options:

* slurm info GROUPNAME
	This command displays the IP of master node and state of worker nodes
* slurm deploy GROUPNAME LOGINNAME
	This command can be used to deploy slurm in a group (Specify the login name used to create the group)
* slurm delete GROUPNAME
	This command can be used to delete a group form the database
	note: This does not delete the actual cluster, it just deletes its entries in database

The hadoop command give the following options:

* hadoop info GROUPNAME
	This command displays the IP of master node
* hadoop deploy GROUPNAME LOGINNAME
	This command can be used to deploy slurm in a group (Specify the login name used to create the group)
* hadoop delete GROUPNAME
	This command can be used to delete a group form the database
	note: This does not delete the actual cluster, it just deletes its entries in database

## Future Scope

* This project has the scope using the checkpoint feature of slurm to store the cluster and restart it at any point
* Extend the project to clouds other than india
* Complete hadoop cluster part of project

## Known Bugs to be fixed

* Cloudmesh stores VM server names with an _ in the end, for example user_1, but the hostname is infact stored with a -, for example user-1. Hostname is essential for slurm deployment. If a user name has an underscore,  for example user_name, then this could cause problems in slurm deployment


## Prerequisites

This project assumes you have a working cloudmesh setup and can create and delete virtual machines.
This project assumes you are using india as your cloud

### Setup

* Download the source code form https://github.com/cloudmesh/cluster
* Place it in the same folder as your cloudmesh folder (beside it not inside it)
* cd to the cluster folder
* install the setup with the command: python setup.py install

### Testing

For testing instructions please see:

* https://github.com/cloudmesh/cluster/blob/master/Test.rst


