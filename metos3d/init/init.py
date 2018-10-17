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
import socket
import glob
import os
import difflib

class Metos3DInitGroup(click.Group):
    
    def list_commands(self, ctx):
        return ["all", "env", "petsc", "data", "model"]
    
    def get_command(self, ctx, name):
        if name in self.list_commands(ctx):
            return metos3d.__getattribute__("init_" + name)
        else:
            None

# init
@click.group("init", cls=Metos3DInitGroup)
@click.pass_context
def init_cli(ctx):
    """Initialize Metos3D"""
    pass

# init all
@init_cli.command("all")
@click.pass_context
def init_all(ctx):
    """Initialize compiler, PETSc, data and models"""
    metos3d.echo("Initializing", "Metos3D")
    # invoke env, petsc, data, model as click.commands
    init_cmd = ctx.parent.command
    for name in ["env", "petsc", "data", "model"]:
        cmd = init_cmd.get_command(ctx, name)
        cmd.invoke(ctx)

# init env
@init_cli.command("env")
#@click.argument("envfile", type=click.File("r"))#, help="environment file")
@click.pass_context
#def init_env(ctx, envfile):
def init_env(ctx):
    """Set Metos3D compiler environment"""
    metos3d.echo("Initializing", "Metos3D compiler environment")
    
    # get host name
    host = socket.getfqdn()
    metos3d.echo("Detecting hostname", host)
    host_reverse = host.split(".")
    host_reverse.reverse()

    # get known environment files
    env_path = ctx.obj.basepath + "/env/*"
    metos3d.echo("Fetching known hostname files", env_path)
    hosts = glob.glob(env_path)
    hosts_file = list(map(os.path.basename, hosts))

    # compare host name and file name
    for file in hosts_file:
        sm = difflib.SequenceMatcher(None, host_reverse, file.split("."))
        # choose only those that match on 3 or more name parts
        smb = [mb for mb in sm.get_matching_blocks() if mb.a==0 and mb.b==0 and mb.size>=3]
#        metos3d.echo("Matching blocks", smb)
        metos3d.echo(file, smb)




# 'a string'[::-1]

#    for file in hosts_file:
#        print("hosts ...", file, file.split("."))


# init petsc
@init_cli.command("petsc")
@click.pass_context
def init_petsc(ctx):
    """Configure and compile PETSc library"""
    metos3d.echo("Initializing", "PETSc library")

# init data
@init_cli.command("data")
@click.pass_context
def init_data(ctx):
    """Set location for Metos3D data"""
    metos3d.echo("Initializing", "Metos3D data")

# init model
@init_cli.command("model")
@click.pass_context
def init_model(ctx):
    """Set location for Metos3D models"""
    metos3d.echo("Initializing", "Metos3D models")



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
#                           label="Downloading PETSc",
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

