# ---------------------------------------------------------------------
# ***p3launcher***
#
# Author:           Pranaw G. Pradhan
# Email:            pranawpradhan@gmail.com
#
# Creation Date:    2022-11-20
# Last Modified on: 
#
# ---------------------------------------------------------------------


if __name__ == '__main__':
    import sys

    sys.dont_write_bytecode = True

    import core
    # print(sys.argv)
    core.run(sys.argv[1:])

