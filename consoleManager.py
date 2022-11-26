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

import platform


class ConsoleManager(object):
    """Console Manager class to determine which console definition to use.
    """

    def __init__(self):
        self.__currentPlatform = platform.system()
        if self.__currentPlatform == 'Windows':
            from console import cmd
            self.__consoleClass = cmd.Cmd

    def getConsole(self):
        """Returns suitable console definition class for this OS.

        :return: un-initialized console definition class
        :rtype: __class__
        """
        return self.__consoleClass
