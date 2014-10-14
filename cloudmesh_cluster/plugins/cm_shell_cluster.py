from cmd3.shell import command
from cloudmesh_common.logger import LOGGER

log = LOGGER(__file__)


class cm_shell_cluster:
    """Creating a virtual cluster"""

    def activate_cm_shell_cluster(self):
        self.register_command_topic('cloud', 'cluster')
        pass

    @command
    def do_cluster(self, args, arguments):
        """
        Usage:
            cluster create NAME WORKERS CLOUD
            cluster info [NAME]
            cluster delete [-f] [NAME]
            cluster clean

        Manages a virttual cluster on a cloud

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

        if arguments["delete"] and arguments["NAME"]:
            log.info("delete the cluster '{NAME}'".format(**arguments))
            return
        elif arguments["delete"]:
            log.info("delete all the clusters")
            return

        if arguments["info"] and arguments["NAME"]:
            log.info("info of cluster {NAME}".format(**arguments))
            return
        elif arguments["info"]:
            log.info("info of all clusters")
            return

        if arguments["list"] and arguments["NAME"]:
            log.info("list of cluster {NAME}".format(**arguments))
            return
        elif arguments["list"]:
            log.info("list of all clusters")
            return

        return
