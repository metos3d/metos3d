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
import yaml
import click

metos3d_conf_file = "metos3d.conf.yaml"
metos3d_conf_message = """
### ERROR: No Metos3D configuration file found


"""

def info_show_configuration(ctx):
    metos3d_conf = load(open(metos3d_conf_file))
    click.echo(metos3d_conf)
    pass

def info_show_message(ctx):
    click.echo(metos3d_conf_message)
    pass

def info(ctx):
    """
        Retrieve information from the configuration file.
    """
    
    
    if os.path.exists(metos3d_conf_file):
        info_show_configuration(ctx)
    else:
        info_show_message(ctx)
