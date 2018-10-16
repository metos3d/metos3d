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
import sys, traceback
import click
import yaml
import metos3d

class Context():
    pass

class Metos3DGroup(click.Group):
    def list_commands(self, ctx):
        return ["info", "env", "petsc", "data", "model", "simpack", "optpack"]

# echo
def echo(item, content):
    text = "{:.<30} {}".format(item, content)
    click.echo(text)

# debug
def debug(ctx, item, content):
    if ctx.obj.verbose:
        text = "[DEBUG]"
        text = text + " {} ... {}".format(item, content)
        click.echo(text)

# error
def error(item, **kwargs):
    text = click.style("[ERROR]", fg="red", bold=True)
    text = text + " {} ...".format(item)
    click.echo(text)
    if kwargs.get("is_exception"):
        traceback.print_exc(1)
    sys.exit(1)

# read metos3d config
def read_configuration(ctx):
    metos3d_conf_file_path = ctx.obj.basepath + "/metos3d.conf.yaml"
    try:
        metos3d.debug(ctx, "Opening Metos3D configuration file", metos3d_conf_file_path)
        with open(metos3d_conf_file_path) as metos3d_conf_file:
            try:
                metos3d.debug(ctx, "Loading Metos3D configuration as YAML file", metos3d_conf_file_path)
                metos3d_conf = yaml.load(metos3d_conf_file)
            except Exception:
                metos3d.error("Can't load Metos3D configuration as YAML file", is_exception=True)
    except Exception:
        metos3d.error("Can't open Metos3D configuration file", is_exception=True)
    return metos3d_conf

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

# info
@metos3d_cli.command("info")
@click.pass_context
def metos3d_info(ctx):
    """Show Metos3D configuration"""
    metos3d.info(ctx)

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






#
#    exc_info
#    with  as exc_info:
#        if exc_info is not None:
#            print(exc_info)
##        kwargs.get("exception").print_exc()
#        traceback.print_last()
##        traceback.print_tb(sys.exc_info()[2])
##        traceback.print_exception(sys.last_type)
##sys.last_value
##sys.last_traceback
##        print(kwargs.get("exception"))
##        click.echo(sys.exc_info()[2].format_exc())

