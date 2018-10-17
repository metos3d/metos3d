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

import click
import yaml
import sys
import traceback

# echo
def echo(item, content):
    text = "{:.<40} {}".format(item + " ", content)
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
    
    # try to open and load config
    try:
        debug(ctx,
              "Opening Metos3D configuration file",
              metos3d_conf_file_path)
        with open(metos3d_conf_file_path) as metos3d_conf_file:
            try:
                debug(ctx,
                      "Loading Metos3D configuration as YAML file",
                      metos3d_conf_file_path)
                metos3d_conf = yaml.load(metos3d_conf_file)
            except Exception:
                error("Can't load Metos3D configuration as YAML file",
                      info="Run 'metos3d init all' first",
                      is_exception=True)
    except Exception:
        error("Can't open Metos3D configuration file",
              info="Run 'metos3d init all' first",
              is_exception=True)

    # try to access the config
    try:
        metos3d_conf["metos3d"]
        metos3d_conf["metos3d"]["env"]
        metos3d_conf["metos3d"]["petsc"]
        metos3d_conf["metos3d"]["data"]
        metos3d_conf["metos3d"]["model"]
    except Exception:
        error("Can't access loaded Metos3D configuration",
              info="Run 'metos3d init all' first",
              is_exception=True)

    return metos3d_conf


