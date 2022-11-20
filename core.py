# ---------------------------------------------------------------------
# ***packages***
#
# Author:           Pranaw G. Pradhan
# Email:            pranawpradhan@gmail.com
#
# Creation Date:    2022-11-20
# Last Modified on: 
#
# ---------------------------------------------------------------------

import os
import argparse
import subprocess
import sys
import imp

import constants


def run(options):
    parser = argparse.ArgumentParser(description='Launching environment using...')
    parser.add_argument('packages', metavar='env', type=str, nargs='+',
                        help='name of packages to include')

    args = parser.parse_args()
    # print args.packages

    foundPackages = []
    for pth in constants.P3LAUNCHPKGPATHS:
        # print pth
        # print os.listdir(pth)
        for pkg in os.listdir(pth):
            foundPackages.append(os.path.join(pth, pkg).replace(os.sep, os.altsep))

    env = Env()
    # pythonPaths = []
    for pkgNameVer in args.packages:
        pkgName, _, pkgVer = pkgNameVer.partition('-')
        if not pkgVer:
            pkgVer = 'dev'
        for pkgPaths in foundPackages:
            # get pkg description file
            if pkgName in pkgPaths:
                verPath = os.path.join(pkgPaths, pkgVer).replace(os.sep, os.altsep)
                mod = importModuleFromPath('p3launchPkg', verPath)
                # env.PATH += mod.PATH
                # env.PYTHONPATH += mod.PYTHONPATH
                mod.commands(env)

    # oEnv = os.environ.copy()
    nEnv = env.getEnv()
    nEnv.update({'P3LAUNCHPKGPATHS': ';'.join(constants.P3LAUNCHPKGPATHS)})

    # cmd = 'prompt $g $c{}$f'.format(options)
    cmd = 'cmd /Q /K prompt $g $c{}$f'.format(' '.join(options))
    # print cmd
    p = subprocess.Popen(cmd, env=nEnv, creationflags=subprocess.CREATE_NEW_CONSOLE)
    # stdout, stderr = p.communicate()
    # sys.exit(p.returncode)
    # p.wait()
    return p


class Env:
    PATH = []
    PYTHONPATH = []

    def getEnv(self):
        return {
            'PATH':  ';'.join(self.PATH),
            'PYTHONPATH':  ';'.join(self.PYTHONPATH)
        }


def importModuleFromPath(moduleName, path, parent=None):
    """

    :param moduleName: module name
    :param path:
    :param parent:
    :return:
    """
    # try:
    #     return sys.modules[moduleName]
    # except KeyError:
    #     pass

    try:
        fp, pathname, stuff = imp.find_module(moduleName, [path])
    except ImportError:
        raise

    imp.acquire_lock()
    try:
        # sys.modules.pop(moduleName, None)
        m = imp.load_module(moduleName, fp, pathname, stuff)
    finally:
        if fp:
            fp.close()
        imp.release_lock()

    if parent:
        setattr(parent, moduleName, m)

    return m
