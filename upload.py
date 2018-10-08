#
# Metos3D: A Marine Ecosystem Toolkit for Optimization and Simulation in 3-D
# Copyright (C) 2018  Jaroslaw Piwonski, CAU, jpi@informatik.uni-kiel.de
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os
import sys

def let_user_decide(cmd):
    print("Proceed? (Y/n/q)")
    answer = input()
    if answer == "q":
        sys.exit(1)
    if answer == "n":
        return
    os.system(cmd)

if __name__ == "__main__":
    '''
        Create an official Metos3D distribution on PyPI and Anaconda.
        
        The following packages must be installed and set:
        $>
            pip install twine
            conda install conda-build
            conda install anaconda-client
            conda config --set anaconda_upload yes
            
        Working branch must not be named as tags are and upload stream must be set up:
        $>
            git co -b 1.0dev
            git push --set-upstream origin 1.0dev
        
        Given a version number as comand line argument the script does the following:
        
            1. create version string in metos3dpy/version.py file
            2. git commit all changes, comment is version number
            3. git tag everything, comment and annotation is version number
            4. git push to github repo
            
            5. setup as pypi package
            6. upload to pypi
            
            7. use conda-skeleton to create recipe
            8. build and upload conda package
            
            9. clean up
        '''
    
    if len(sys.argv[:]) < 2:
        print("usage: python {0} [version]".format(sys.argv[0]))
        print("example:")
        print("$> python {0} 1.0.0".format(sys.argv[0]))
        print("current:")
        cmd = "git branch -avvv"
        print("$> " + cmd)
        os.system(cmd)
        cmd = "git describe --always"
        print("$> " + cmd)
        os.system(cmd)
        cmd = "cat metos3dpy/version.py"
        print("$> " + cmd)
        os.system(cmd)
        sys.exit(0)

    version = sys.argv[1]
    print("Preparing version ....... " + version)

    cmd = "cd metos3dpy/; echo '__version__ = \"{0}\"' > version.py ".format(version)
    print("Writing version ......... " + cmd)
    let_user_decide(cmd)

    cmd = "git ci -am '{0}'".format(version)
    print("Commiting ............... " + cmd)
    let_user_decide(cmd)

    cmd = "git tag -a -m '{0}' {0}".format(version)
    print("Tagging ................. " + cmd)
    let_user_decide(cmd)

    cmd = "git push --follow-tags"
    print("Pushing ................. " + cmd)
    let_user_decide(cmd)

    cmd = "python setup.py sdist"
    print("Creating distribution ... " + cmd)
    let_user_decide(cmd)

    cmd = "twine upload dist/metos3d-{0}.tar.gz".format(version)
    print("Uploading to PyPI ....... " + cmd)
    let_user_decide(cmd)

    cmd = "mkdir -p conda-recipe"
    print("Creating ................. " + cmd)
    let_user_decide(cmd)

    cmd = "cd conda-recipe/; conda-skeleton pypi --noarch-python metos3d"
    print("Creating recipe ......... " + cmd)
    let_user_decide(cmd)

    cmd = "cd conda-recipe/; conda-build metos3d"
    print("Building and uploading .. " + cmd)
    let_user_decide(cmd)

    cmd = "conda build purge"
    print("Cleaning up ............. " + cmd)
    let_user_decide(cmd)

    cmd = "rm -fr dist/*"
    print("Cleaning up ............. " + cmd)
    let_user_decide(cmd)

    cmd = "rm -fr conda-recipe/*"
    print("Cleaning up ............. " + cmd)
    let_user_decide(cmd)

#    cmd = "rm -fr metos3d.egg-info/"
#    print("Cleaning up ............. " + cmd)
#    let_user_decide(cmd)


