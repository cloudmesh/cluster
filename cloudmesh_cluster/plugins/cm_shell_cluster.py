from cmd3.shell import command
from cloudmesh_common.logger import LOGGER
import cloudmesh
from cloudmesh_cluster.api.virtual_cluster import virtual_cluster

log = LOGGER(__file__)


class cm_shell_cluster:
    """Creating a virtual cluster"""

    def activate_cm_shell_cluster(self):
        self.register_command_topic('cloud', 'slurm')
        pass

    @command
    def do_slurm(self, args, arguments):
        """
        Usage:
            slurm create NAME WORKERS CLOUD [--image=IMAGE] [--flavor=FLAVOR]
            slurm info [NAME]
            slurm status [NAME]            
            slurm delete [-f] [NAME]
            slurm clean
            slurm checkpoint NAME
            slurm restore NAME
            slurm list
            slurm default NAME WORKERS CLOUD [--image=IMAGE] [--flavor=FLAVOR]

        Manages a virtual cluster on a cloud

        Arguments:

          NAME     The name of the cluster
          WORKERS  The number of workers in the virtual cluster
          CLOUD    The name of the cloud on which the virtual cluster
                   is to be deployed

        Options:

           -v       verbose mode

        """
        log.info(arguments)

        if arguments["clean"]:
            log.info("clean the vm")
            return

        if arguments["default"] and arguments["NAME"] and arguments["WORKERS"] and arguments["CLOUD"]:
           virtual_cluster().defaults("{NAME}".format(**arguments),"{WORKERS}".format(**arguments),"{CLOUD}".format(**arguments),"{--image}".format(**arguments),"{--flavor}".format(**arguments))
           return

        if arguments["create"] and arguments["NAME"] and arguments["WORKERS"] and arguments["CLOUD"]:
           virtual_cluster().create("{NAME}".format(**arguments),"{WORKERS}".format(**arguments),"{CLOUD}".format(**arguments),"{--image}".format(**arguments),"{--flavor}".format(**arguments))
           return
        elif arguments["create"]:
           virtual_cluster().create_defaults()
           return

        if arguments["delete"] and arguments["NAME"]:
            virtual_cluster().delete("{NAME}".format(**arguments))
            log.info("delete the cluster '{NAME}'".format(**arguments))
            return
        elif arguments["delete"]:
            virtual_cluster().delete_all()
            log.info("delete all the clusters")
            return

        if arguments["info"] and arguments["NAME"]:
            virtual_cluster().info("{NAME}".format(**arguments))
            log.info("info of cluster {NAME}".format(**arguments))
            return
        elif arguments["info"]:
            virtual_cluster().info_all()
            log.info("info of all clusters")
            return

        if arguments["list"]:
            virtual_cluster().list_clusters()
            log.info("list of all clusters")
            return

        return
