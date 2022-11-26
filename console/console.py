# ---------------------------------------------------------------------
# ***packages***
#
# Author:           Pranaw G. Pradhan
# Email:            pranawpradhan@gmail.com
#
# Creation Date:    2022-11-26
# Last Modified on: 
#
# ---------------------------------------------------------------------

import subprocess


class Console(object):
    """Abstract console object

    :ivar packages: name of packages
    :type packages: list of str

    :ivar env: environment declaration for subprocess
    :type env: dict

    :cvar _coreCommands: list of core commands (constant, do not modify)
    :type _coreCommands: list of str

    :ivar userCommands: list of user defined commands
    :type userCommands: list of str

    """

    def __init__(self, *args, **kwargs):
        self.packages = kwargs.get('packages', [])
        self.env = kwargs.get('env', None)
        self._coreCommands = None
        self.userCommands = None

    def getCommand(self):
        return ' '.join(self._coreCommands + self.userCommands)

    def getCommandTokens(self):
        return self._coreCommands + self.userCommands

    def run(self):
        """Runs new process with the given env and commands

        :return: new process status
        """
        cmd = self.getCommandTokens()
        p = subprocess.Popen(cmd, env=self.env)
        p.communicate()
        return p
