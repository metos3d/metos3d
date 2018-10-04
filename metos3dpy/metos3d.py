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
import socket
import click
import yaml
import metos3dpy

class Context():
    pass

@click.group("metos3d")
@click.help_option("-h", "--help")
@click.version_option(metos3dpy.__version__, "-V", "--version")
@click.option("-v", "--verbose", is_flag=True, help="Show invoked shell commands and their output.")
@click.pass_context
def metos3d(ctx, verbose):
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

@metos3d.command("config")
@click.pass_context
def metos3d_config(ctx):
    """Show/Configure Metos3D environment."""
    metos3dpy.config(ctx)

@metos3d.command("simpack")
@click.pass_context
def metos3d_simpack(ctx):
    """Prepare simulation experiment."""
    metos3dpy.simpack(ctx)

@metos3d.command("optpack")
@click.pass_context
def metos3d_optpack(ctx):
    """Prepare optimization experiment."""
    metos3dpy.optpack(ctx)


