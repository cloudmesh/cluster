from cmd3.shell import command
from cloudmesh_common.logger import LOGGER
import cloudmesh
from cloudmesh_slurm.api.virtual_hadoop import virtual_hadoop

log = LOGGER(__file__)


class cm_shell_hadoop:
    """Creating a hadoop cluster"""

    def activate_cm_shell_hadoop(self):
        self.register_command_topic('platform', 'hadoop')
        pass

    @command
    def do_hadoop(self, args, arguments):
        """
        Usage:
            hadoop create GROUPNAME DATANODES
            hadoop info [GROUPNAME]

        Manages a hadoop cluster on a cloud

        Arguments:

          NAME       The name of the hadoop cluster
          DATANODES  The number of datanodes in the hadoop cluster


        Options:

           -v       verbose mode

        """
        log.info(arguments)

        if (arguments["create"] and
            arguments["GROUPNAME"] and
            arguments["DATANODES"]):
            virtual_hadoop().create("{GROUPNAME}".format(**arguments),
                                    "{DATANODES}".format(**arguments),"india")
            return

        return
