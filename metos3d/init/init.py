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
import metos3d

class Metos3DInitGroup(click.Group):
    
    def list_commands(self, ctx):
        return ["all", "env", "petsc", "data", "model"]
    
    def get_command(self, ctx, name):
        print(self, ctx, name)
        if name in self.list_commands(ctx):
            return metos3d.__getattribute__("init_" + name)
        else:
            None

# init
@click.group("init", cls=Metos3DInitGroup)
@click.pass_context
def init_cli(ctx):
    """Initialize Metos3D"""
    print(ctx.obj)
    pass

# init all
@init_cli.command("all")
@click.pass_context
def init_all(ctx):
    """Initialize env, petsc, data, model"""
    print(ctx.obj)
    pass

# init env
@init_cli.command("env")
@click.pass_context
def init_env(ctx):
    """Initialize env"""
    print(ctx.obj)
    pass

# init petsc
@init_cli.command("petsc")
@click.pass_context
def init_petsc(ctx):
    """Initialize petsc"""
    print(ctx.obj)
    pass

# init data
@init_cli.command("data")
@click.pass_context
def init_data(ctx):
    """Initialize data"""
    print(ctx.obj)
    pass

# init model
@init_cli.command("model")
@click.pass_context
def init_model(ctx):
    """Initialize model"""
    print(ctx.obj)
    pass



#import re
#import os
#import sys
#import traceback
#import glob
#import click
#import socket
#import subprocess
#        import traceback
#        traceback.print_last()
##        traceback.print_exception(sys.last_type)
##sys.last_value
##sys.last_traceback

#        print(sys.last_traceback)
#    if metos3d_conf["metos3d"]["version"] is None:
#        print("version is not set ...")
#        print("Setting version ...", metos3d.__version__)
#        metos3d_conf["metos3d"]["version"] = metos3d.__version__
#
#        with open(metos3d_conf_file, "w") as f:
#            f.write(yaml.dump(metos3d_conf, default_flow_style=False))
#    else:
#
#    if metos3d_conf["metos3d"]["env"] is None:
#        print("env is not set ...")
#
#        host = socket.getfqdn()
#        host_part = host.split(".")
#        host_part.reverse()
#        print("host ...", host, host_part)
#
#        hosts = glob.glob(ctx.obj.basepath + "/env/*")
#        hosts_file = list(map(os.path.basename, hosts))
#        for file in hosts_file:
#            print("hosts ...", file, file.split("."))
#
#    else:
#
#    if metos3d_conf["metos3d"]["petsc"] is None:
#        print("petsc is not set ...")
#
#    if metos3d_conf["metos3d"]["data"] is None:
#        print("data is not set ...")
#
#    if metos3d_conf["metos3d"]["model"] is None:
#        print("model is not set ...")



#    ctx.item_list = [
#                     ["environment.+metos3d-petsc-python2",             "Creating environment"],
#                     ["Configuring PETSc to compile on your system",    "Configuring PETSc"],
#                     ["download.+YAML",                                 "Downloading YAML"],
#                     ["Running configure on YAML",                      "Configuring YAML"],
#                     ["Running make on YAML",                           "Compiling YAML"],
#                     ["Running make install on YAML",                   "Installing YAML"],
#                     ["TESTING:",                                       "Configuring PETSc"],
#                     ["download.+HDF5",                                 "Downloading HDF5"],
#                     ["Running configure on HDF5",                      "Configuring HDF5"],
#                     ["Running make on HDF5",                           "Compiling HDF5"],
#                     ["Running make install on HDF5",                   "Installing HDF5"],
#                     ["TESTING:",                                       "Configuring PETSc"],
#                     ["download.+FBLASLAPACK",                          "Downloading FBLASLAPACK"],
#                     ["Compiling FBLASLAPACK",                          "Compiling FBLASLAPACK"],
#                     ["TESTING:",                                       "Configuring PETSc"],
#                     ["make PETSC_DIR=.+PETSC_ARCH=",                   "Compiling PETSc"],
#                     ["environment.+metos3d-petsc-python2",             "Removing environment"],
#                     ]


#    ctx.item = "Starting"
#
#    # set compiler variables, CC, CXX,FC

#cd ctx.obj.basepath / petsc/;
#source ../env/generic.mpich.gcc.env.sh
#source ../env/de.dkrz.mistral.intelmpi.env.sh
#source ../env/de.uni-kiel.rz.rzcluster.env.sh
#...
#;
#source petsc.conf.sh

##    cmd_env = "source " + ctx.obj.basepath + "/env/generic.mpich.gcc.env.sh"
##    cmd_env = "source " + ctx.obj.basepath + "/env/de.dkrz.mistral.intelmpi.env.sh"
#    cmd_env = "source " + ctx.obj.basepath + "/env/de.uni-kiel.rz.rzcluster.env.sh"
#    cmd_petsc = "source " + ctx.obj.basepath + "/petsc/petsc.conf.sh"
#    cmd = cmd_env + ";" + cmd_petsc
#    proc = subprocess.Popen(cmd,
#                            shell=True,
#                            stdout=subprocess.PIPE,
#                            stderr=subprocess.STDOUT)
#
#    # test on dkrz
#    # time . ../../metos3d/petsc/petsc.conf.sh > petsc_configure_lines.txt &
#    # wc petsc_configure_lines.txt
#    # 2146   5626 176734 petsc_configure_lines.txt
#    with click.progressbar(length=2200,
#                           width=0,
#                           label="metos3d init",
#                           ) as bar:
#
#        pattern = ctx.item_list.pop(0)
#        for item in bar:
#            out = proc.stdout.readline().decode("utf-8")
##            print(out.strip())
#            m = re.search(pattern[0], out) if pattern else None
#            if m:
#                bar.label = pattern[1]
#                pattern = ctx.item_list.pop(0) if ctx.item_list else None

