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
import glob
import socket
import click
import yaml
import metos3d

class Context():
    pass

class Metos3DGroup(click.Group):
    def list_commands(self, ctx):
        return ["info", "env", "petsc", "data", "model", "simpack", "optpack"]

@click.command("metos3d", cls=Metos3DGroup, invoke_without_command=True)
#@click.command("metos3d", cls=Metos3DGroup)
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

    print(ctx.invoked_subcommand)
    if ctx.invoked_subcommand is None:
        print(ctx.get_help())

# info
@metos3d_cli.command("info")
@click.pass_context
def metos3d_info(ctx):
    """Show Metos3D configuration"""
    print(metos3d_info.__doc__)

# env
@metos3d_cli.command("env")
@click.pass_context
def metos3d_env(ctx):
    """Configure Metos3D compiler environment"""
    print(metos3d_env.__doc__)

# petsc
@metos3d_cli.command("petsc")
@click.pass_context
def metos3d_petsc(ctx):
    """Configure PETSc library"""
    print(metos3d_petsc.__doc__)

# data
@metos3d_cli.command("data")
@click.pass_context
def metos3d_data(ctx):
    """Configure Metos3D data"""
    print(metos3d_data.__doc__)

# model
@metos3d_cli.command("model")
@click.pass_context
def metos3d_model(ctx):
    """Configure Metos3D BGC models"""
    print(metos3d_model.__doc__)

# simpack
@metos3d_cli.command("simpack")
@click.pass_context
def metos3d_simpack(ctx):
    """Prepare Metos3D simulation experiment"""
    print(metos3d_simpack.__doc__)

# optpack
@metos3d_cli.command("optpack")
@click.pass_context
def metos3d_optpack(ctx):
    """Prepare Metos3D optimization experiment"""
    print(metos3d_optpack.__doc__)


