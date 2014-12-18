Prerequisites
=============

You should be able to create clusters with the cluster command. This requires you to setup a default cloud, image and flavor

Testing Instructions for Slurm
=============

* cd to the cluster directory
* Launch cloudmesh commandline using 'cm' command
* Create a cluster with the cluster command.
	Example: cluster create --count=4 --group=test1 --ln=ubuntu
* Deploy slurm on the cluster using slurm deploy command (specify the login name used to create your cluster).
	Example: slurm deploy test1 ubuntu
* Check the status of the cluster with slurm info command.
	Example: slurm info test1
* Try to install slurm again repeating the above step
* Delete the group from database using slurm delete command
	Example: slurm delete test1 
* ssh to the master node of your cluster and submit a simple command.
	Example: slurm info test1 (get master node)
		ssh -l ubuntu xxx.xxx.xxx.xxx (IP address of master node)
		srun -n2 hostname (displays hostname of each worker node)

Testing Instructions for Hadoop
=============

* cd to the cluster directory
* Launch cloudmesh commandline using 'cm' command
* Create a cluster with the cluster command.
	Example: cluster create --count=4 --group=test1 --ln=ubuntu
* Deploy hadoop on the cluster using hadoop deploy command (specify the login name used to create your cluster).
	Example: hadoop deploy test1 ubuntu
* Check the status of the cluster with hadoop info command.
	Example: hadoop info test1
* Try to install hadoop again repeating the above step
* Delete the group from database using hadoop delete command
	Example: hadoop delete test1

