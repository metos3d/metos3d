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

if __name__ == "__main__":
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


#git push --set-upstream origin refs/heads/1.0.4:refs/heads/1.0.4
#git push --follow-tags --set-upstream origin refs/heads/1.0.4:refs/heads/1.0.4

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
