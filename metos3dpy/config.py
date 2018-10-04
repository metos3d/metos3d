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

from .util import check_conf

def config(ctx):
    check_conf()
#    if is_metos3d_configured():
#        show_configuration(ctx)
#    else:
#        configure_metos3d(ctx)

#    check_conf()
#    if not os.path.exists("metos3d.conf.yaml"):
#        print("no configuration file found ...")

    print("metos3dpy/config.py", ctx)
    print("metos3dpy/config.py", ctx.obj)

#def show_configuration(ctx):
#    print("show configuration ...")
#    pass
#
#def configure_metos3d(ctx):
#    print("configure metos3d ...")
#    pass
