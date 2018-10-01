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

git co -b 1.0-dev
git push --set-upstream origin 1.0-dev

import os
import sys

if __name__ == "__main__":
    '''
        Create an official Metos3D distribution on PyPI and Anaconda.
        
        The following packages must be installed:
        $>
            pip install twine
            conda install conda-build
            conda install anaconda-client
            
        Working branch must not be named as tags are and upload stream must be set up:
        $>
            git co -b 1.0.0dev
            git push --set-upstream origin 1.0.0dev
        
        Given a version number as comand line argument the script does the following:
        
            1. create version string in metos3dpy/version.py file
            2. git commit all changes, comment is version number
            3. git tag everything, comment and annotation is version number
            4. git push to github repo
            
        
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
        sys.exit(0)

    version = sys.argv[1]
    print("Preparing version ....... " + version)

    version_file = "metos3dpy/version.py"
    print("Writing to .............. " + version_file)
    f = open(version_file, "w", encoding="utf-8")
    f.write("__version__ = \"{0}\"\n".format(version))
    f.close()

    cmd = "git ci -am '{0}'".format(version)
    print("Commiting ............... " + cmd)
    os.system(cmd)

    cmd = "git tag -a -m '{0}' {0}".format(version)
    print("Tagging ................. " + cmd)
    os.system(cmd)

    cmd = "git push --follow-tags"
    print("Pushing ................. " + cmd)
    os.system(cmd)

#    cmd = "python setup.py sdist"
#    print("Creating distribution ... " + cmd)
#    os.system(cmd)

#cmd = "twine upload dist/metos3d-{0}.tar.gz".format(version)
#print("Uploading to PyPI ....... " + cmd)
#os.system(cmd)



#conda config --set anaconda_upload yes
