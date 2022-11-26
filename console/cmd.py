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

from . import console


class Cmd(console.Console):
    """Console definition for windows command prompt
    """

    def __init__(self, *args, **kwargs):
        super(Cmd, self).__init__(*args, **kwargs)
        self._coreCommands = ['cmd', '/Q', '/K', 'prompt', '$g', '$c{}$f'.format(' '.join(self.packages))]
        self.userCommands = list()
