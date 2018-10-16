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
import traceback
import click
import yaml
import metos3d

class Context():
    pass

class Metos3DGroup(click.Group):
    
    def list_commands(self, ctx):
        return ["init", "info", "simpack", "optpack"]
    
    def get_command(self, ctx, name):
        print(self, ctx, name)
        return metos3d.__getattribute__(name + "_cli")

# echo
def echo(item, content):
    text = "{:.<30} {}".format(item + " ", content)
    click.echo(text)

# debug
def debug(ctx, item, content):
    if ctx.obj.verbose:
        text = text = click.style("[DEBUG]", bold=True)
        text = text + " {} ... {}".format(item, content)
        click.echo(text)

# error
def error(item, **kwargs):
    # error message
    text = click.style("[ERROR]", fg="red", bold=True)
    text = text + " {} ...".format(item)
    click.echo(text)
    # exception message
    if kwargs.get("is_exception"):
        traceback.print_exc(1)
    # info message
    if kwargs.get("info"):
        text = click.style("[INFO]", fg="green", bold=True)
        text = text + " {} ...".format(kwargs["info"])
        click.echo(text)
    sys.exit(1)

# read metos3d config
def read_config(ctx):
    metos3d_conf_file_path = ctx.obj.basepath + "/metos3d.conf.yaml"
    try:
        metos3d.debug(ctx, "Opening Metos3D configuration file", metos3d_conf_file_path)
        with open(metos3d_conf_file_path) as metos3d_conf_file:
            try:
                metos3d.debug(ctx, "Loading Metos3D configuration as YAML file", metos3d_conf_file_path)
                metos3d_conf = yaml.load(metos3d_conf_file)
            except Exception:
                metos3d.error("Can't load Metos3D configuration as YAML file",
                              info="Run 'metos3d init all' first",
                              is_exception=True)
    except Exception:
        metos3d.error("Can't open Metos3D configuration file",
                      info="Run 'metos3d init all' first",
                      is_exception=True)
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

    print(ctx.obj)


