from cmd3.shell import command
from cloudmesh_common.logger import LOGGER
import cloudmesh
from cloudmesh_slurm.api.virtual_hadoop import virtual_hadoop

log = LOGGER(__file__)


class cm_shell_hadoop:
    """Creating a hadoop cluster"""

    def activate_cm_shell_hadoop(self):
        self.register_command_topic('cloud', 'hadoop')
        pass

    @command
    def do_hadoop(self, args, arguments):
        """
        Usage:
            hadoop create NAME DATANODES
            hadoop info [NAME]

        Manages a hadoop cluster on a cloud

        Arguments:

          NAME       The name of the hadoop cluster
          DATANODES  The number of datanodes in the hadoop cluster


        Options:

           -v       verbose mode

        """
        log.info(arguments)

        if (arguments["create"] and
            arguments["NAME"]
            and arguments["DATANODE"]) :
            virtual_hadoop_cluster().create("{NAME}".format(**arguments),
                                            "{DATANODDES}".format(**arguments))
            return

        return

