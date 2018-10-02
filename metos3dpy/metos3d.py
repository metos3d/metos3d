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
import yaml
import metos3dpy

# context
class Context():
    pass

# metos3d command group
@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.option("-v", "--verbose", is_flag=True, help="Show invoked shell commands and their output.")
@click.version_option(metos3dpy.__version__, "-V", "--version")
@click.pass_context
def metos3d(ctx, verbose):
    '''
        Metos3D: A Marine Ecosystem Toolkit for Optimization and Simulation in 3-D
        
        \b
        Sources:
        https://github.com/metos3d
        
        \b
        Scientific article:
        [Piwonski and Slawig, 2016]
        https://www.geosci-model-dev.net/9/3729/2016
        
        '''
    
    ctx.obj = Context()
    ctx.obj.verbose = verbose
    print("# metos3d:", ctx.obj)
    print("# verbose:", ctx.obj.verbose)

    print(os.getcwd())                  # current working directory
    print(os.path.realpath(__file__))   # script directory

# info command
@metos3d.command()
@click.pass_context
def info(ctx):
    '''
        Show Metos3D configuration.
        '''
    
    print("# info:   ", ctx.obj)
    print("# verbose:", ctx.obj.verbose)
    pass

# init command
# env, petsc
@metos3d.command()
@click.pass_context
def init(ctx):
    '''
        Initialize Metos3D environment.
        '''
    
    print("# init:   ", ctx.obj)
    print("# verbose:", ctx.obj.verbose)
    pass

# simpack command
@metos3d.command()
@click.pass_context
def simpack(ctx):
    '''
        Prepare simulation experiment.
        '''
    print("# metos3d:", ctx.obj)
    print("# verbose:", ctx.obj.verbose)
    pass

# optpack command
@metos3d.command()
@click.pass_context
def optpack(ctx):
    '''
        Prepare optimization experiment.
        '''

    print("# metos3d:", ctx.obj)
    print("# verbose:", ctx.obj.verbose)
    pass

# data command
@metos3d.command()
@click.pass_context
def data(ctx):
    '''
        Configure Metos3D data.
        '''
    
    print("# metos3d:", ctx.obj)
    print("# verbose:", ctx.obj.verbose)
    pass

# model command
@metos3d.command()
@click.pass_context
def model(ctx):
    '''
        Show Metos3D models.
        '''
    
    print("# metos3d:", ctx.obj)
    print("# verbose:", ctx.obj.verbose)
    pass


