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
import click
import metos3d

class Context():
    pass

class Metos3DGroup(click.Group):
    
    def list_commands(self, ctx):
        return ["init", "info", "simpack", "optpack"]
    
    def get_command(self, ctx, name):
        if name in self.list_commands(ctx):
            return metos3d.__getattribute__(name + "_cli")
        else:
            None

# metos3d
@click.command("metos3d", cls=Metos3DGroup)
@click.help_option("-h", "--help")
@click.version_option(metos3d.__version__, "-V", "--version")
@click.option("-v", "--verbose", is_flag=True, help="Show invoked shell commands and their output.")
@click.pass_context
def metos3d_cli(ctx, verbose):
    """
        Metos3D: A Marine Ecosystem Toolkit for Optimization and Simulation in 3-D
        
        \b
        Sources and documentation:
        https://github.com/metos3d
        
        \b
        Scientific article:
        [Piwonski and Slawig, 2016]
        https://www.geosci-model-dev.net/9/3729/2016
    """
    ctx.obj = Context()
    ctx.obj.verbose = verbose
    ctx.obj.basepath = os.path.dirname(__file__)
    
    metos3d.debug(ctx, "Metos3D version", metos3d.__version__)
    metos3d.debug(ctx, "Metos3D path", ctx.obj.basepath)


