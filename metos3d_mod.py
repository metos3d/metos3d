#
# Metos3D: A Marine Ecosystem Toolkit for Optimization and Simulation in 3-D
# Copyright (C) 2013  Jaroslaw Piwonski, CAU, jpi@informatik.uni-kiel.de
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

# import used modules
import os
import sys
import subprocess

########################################################################
### output
########################################################################

# print_error
def print_error(msg):
    print "### ERROR: " + msg

# print_usage
def print_usage():
    print "Usage:"
    print "  metos3d simpack [MODELNAME...]"
#    print "  metos3d update"
#    print "  metos3d update  [all | self | data | model | simpack]"
#    print "  metos3d help    [all | self | data | model | simpack]"

########################################################################
### shell command execution
########################################################################

# execute_command
def execute_command(cmd):#, msg, errmsg):
    print "### EXECUTING: " + cmd
    # execute
    proc = subprocess.Popen(cmd, shell = True)
    out  = proc.communicate()
    # check for error
    if not proc.returncode == 0:
        print "#"
        print "#   Okay, this shouldn't happen ..."
        print "#"
        print "#   The command:", cmd
        print "#   Returned:", proc.returncode
        print "#   We expected: 0, i.e. a success."
        print "#"
        print "#   What now?"
        print "#   1. If you understand, what went wrong, solve the problem and rerun the script."
        print "#   2. If you need help, contact jpi@informatik.uni-kiel.de, attach the output of the script and kindly ask for help."
        print "#"
        sys.exit(1)

########################################################################
### update
########################################################################

## update_self
#def update_self():
#    print "# Selfupdate ..."
#    # update metos3d
#    cmd = "cd " + m3ddir + "/metos3d/; git pull; cd ../../"
#    msg = "# Selfupdate successfully applied."
#    errmsg = "Could not update myself."
#    if not execute_command(cmd, msg, errmsg) == 0: sys.exit(0)
#
## update_data
#def update_data():
#    print "# Updating data ..."
#    # update data
#    cmd = "cd " + m3ddir + "/data/; git pull; cd ../../"
#    msg = "# Data update successfully applied."
#    errmsg = "Could not update data."
#    if not execute_command(cmd, msg, errmsg) == 0: sys.exit(0)
#
## update_model
#def update_model():
#    print "# Updating model ..."
#    # update model
#    cmd = "cd " + m3ddir + "/model/; git pull; cd ../../"
#    msg = "# Model update successfully applied."
#    errmsg = "Could not update model."
#    if not execute_command(cmd, msg, errmsg) == 0: sys.exit(0)
#
## update_simpack
#def update_simpack():
#    print "# Updating simpack ..."
#    # update simpack
#    cmd = "cd " + m3ddir + "/simpack/; git pull; cd ../../"
#    msg = "# Simpack update successfully applied."
#    errmsg = "Could not update simpack."
#    if not execute_command(cmd, msg, errmsg) == 0: sys.exit(0)
#
## update_all
#def update_all():
#    print "# Updating all ..."
#    update_self()
#    update_data()
#    update_model()
#    update_simpack()
#    print "# All packages successfully updated."

########################################################################
### compile
########################################################################

# compile_simpack
def compile_simpack(prefix, modelname):
    modeldir = prefix + "/.metos3d/model/model/" + modelname
    # no model dir
    if not os.path.exists(modeldir):
        print_error("Model directory '" + modeldir + "' does not exist.")
    # compile model
    else:
        # check PETSc variables
        try:
            petscdir = os.environ["PETSC_DIR"]
            petscarch = os.environ["PETSC_ARCH"]
        except KeyError:
            print_error("PETSc variables are not set.")
            sys.exit(1)
        # create links
        # data
        cmd = "if ! [ -e data ]; then ln -s ~/.metos3d/data/data; fi"
        execute_command(cmd)
        # model
        cmd = "if ! [ -e model ]; then ln -s ~/.metos3d/model/model; fi"
        execute_command(cmd)
        # simpack
        cmd = "if ! [ -e simpack ]; then ln -s ~/.metos3d/simpack; fi"
        execute_command(cmd)
        # Makefile
        cmd = "if ! [ -e Makefile ]; then ln -s ~/.metos3d/metos3d/Makefile; fi"
        execute_command(cmd)
        # make clean
        execute_command("make BGC=model/" + modelname + " clean")
        # make
        execute_command("make BGC=model/" + modelname)
        # option
        cmd = "mkdir -p option"
        execute_command(cmd)

        # copy test option file
        filepath = "option/test." + modelname + ".option.txt"
        cmd = "if ! [ -e " + filepath + " ]; then cp model/" + modelname + "/option/test." + modelname + ".option.txt " + filepath + ";fi"
        execute_command(cmd)
        # work
        cmd = "mkdir -p work"
        execute_command(cmd)

########################################################################
### help
########################################################################

## help_model
#def help_model():
#    print "# Listing available models ..."
#    # list models
#    cmd = "ls -al " + m3ddir + "/model/"
#    msg = "# End of list"
#    errmsg = "Could not show available models."
#    if not execute_command(cmd, msg, errmsg) == 0: sys.exit(0)

########################################################################
### subcommand dispatch
########################################################################

# dispatch_simpack
def dispatch_simpack(prefix, argv):
    # no model
    if len(argv) < 3:
        execute_command("ls " + prefix + "/.metos3d/model/model");
    # compile
    else:
        compile_simpack(prefix, argv[2])

## dispatch_update
#def dispatch_update(argv):
#    print "# Update ..."
#    # no subcommand
#    if len(argv) < 3:
#        errmsg = "No subcommand given."
#        print_error([errmsg])
#        print_usage_update()
#        return "not updated"
#    # all
#    status = "unknown"
#    if argv[2] == "all":
#        status = update_all()
#    # self
#    if argv[2] == "self":
#        status = update_self()
#    # data
#    if argv[2] == "data":
#        status = update_data()
#    # model
#    if argv[2] == "model":
#        status = update_model()
#    # simpack
#    if argv[2] == "simpack":
#        status = update_simpack()
#    # unknown
#    if status == "unknown":
#        errmsg = "Unknown subcommand: " + argv[2]
#        print_error([errmsg])
#        print_usage()
#    return status

## dispatch_help
#def dispatch_help(argv):
#    print "# Help ..."
#    # no subcommand
#    if len(argv) < 3:
#        errmsg = ["No subcommand given."]
#        print_error(errmsg)
#        print_usage_help()
#        return "no help showed"
#    # all
#    status = "unknown"
#    if argv[2] == "all":
#        status = help_all()
#    # self
#    if argv[2] == "self":
#        status = help_self()
#    # data
#    if argv[2] == "data":
#        status = help_data()
#    # model
#    if argv[2] == "model":
#        status = help_model()
#    # simpack
#    if argv[2] == "simpack":
#        status = help_simpack()
#    # unknown
#    if status == "unknown":
#        errmsg = ["Unknown subcommand: " + argv[2]]
#        print_error(errmsg)
#        print_usage()
#    return status

########################################################################
### main dispatch
########################################################################

# dispatch_command
def dispatch_command(prefix, argv):
    # simpack
    if argv[1] == "simpack":
        dispatch_simpack(prefix, argv)
#    # update
#    if argv[1] == "update":
#        status = dispatch_update(argv)
#    # help
#    if argv[1] == "help":
#        status = dispatch_help(argv)
    # unknown
    else:
        print_error("Unknown command: " + argv[1])



#
#   PETSc
#

#check PETSc variables

#curl -O ftp://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc-lite-3.3-p7.tar.gz
#gunzip petsc-lite-3.3-p7.tar.gz
#tar xf petsc-lite-3.3-p7.tar or tar xf petsc-lite-3.3-p7.tar -C petsc
#ln -fs petsc-lite-
#cd petsc-3.3-p7/
#./configure

#PETSc:
#    PETSC_ARCH: arch-darwin-c-debug
#    PETSC_DIR: /Users/jpicau/.metos3d/petsc/petsc-3.3-p7
#    Clanguage: C
#    Scalar type: real
#    Precision: double
#    Memory alignment: 16
#    shared libraries: disabled
#    dynamic loading: disabled
#xxx=========================================================================xxx
#    Configure stage complete. Now build PETSc libraries with (cmake build):
#        make PETSC_DIR=/Users/jpicau/.metos3d/petsc/petsc-3.3-p7 PETSC_ARCH=arch-darwin-c-debug all
#    or (experimental with python):
#        PETSC_DIR=/Users/jpicau/.metos3d/petsc/petsc-3.3-p7 PETSC_ARCH=arch-darwin-c-debug ./config/builder.py
#xxx=========================================================================xxx

#proc = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
#out  = proc.communicate()
## check for error
#if not proc.returncode == 0:
#
#>>> for line in out[0].split("\n"):
#...     match = re.search("^  PETSC_ARCH: (.+)", line)
#...     if match: petscarch = match.groups()[0]
#...     match = re.search("^  PETSC_DIR: (.+)", line)
#...     if match: petscdir = match.groups()[0]
#...
#>>> print petscarch
#arch-darwin-c-debug
#>>> print petscdir
#/Users/jpicau/.metos3d/petsc/petsc-3.3-p7

#make PETSC_DIR=~/.metos3d/petsc/petsc PETSC_ARCH=arch-darwin-c-debug all
#make PETSC_DIR=/Users/jpicau/Documents/ARBEIT/CODE/TEST/PETSc/INSTALL/petsc-3.3-p7 PETSC_ARCH=arch-darwin-c-debug test
#export PETSC_DIR=/Users/jpicau/Documents/ARBEIT/CODE/TEST/PETSc/INSTALL/petsc-3.3-p7
#export PETSC_ARCH=arch-darwin-c-debug



#
#   DUMP
#

#    print "# DEBUG: Status:", status

#export PETSC_DIR=/gfs/work-sh1/sunip194/CODE/petsc/petsc-3.3-p5
#export PETSC_ARCH=arch-linux2-c-opt

#    # info
#    print "#"
#    print "#   Compiled executable: metos3d-simpack-" + modelname + ".exe"
#    #print "#   Metos3D simulation package and " + modelname + " has been successfully compiled."
#    print "#"



## compile_model
#def compile_model(modelname):
#    print "# MODELNAME:", modelname
#    modeldir = m3ddir + "/model/" + modelname
#    # no model dir
#    if not os.path.exists(modeldir):
#        print_error("Model directory does not exist: " + modeldir)
#        compile_model_show()
#        return "not compiled"
#    # compile model
#    else:
#        cmd = "cd " + m3ddir + "/simpack/; cd ../../"
#        msg = "# Successfully compiled " + modelname + " model."
#        errmsg = "Could not compile " + modelname + " model."
#        if not execute_command(cmd, msg, errmsg) == 0: sys.exit(0)

## print_usage_simpack
#def print_usage_simpack():
#    execute_command("ls ~/.metos3d/model/model");

## print_usage_compile
#def print_usage_compile():
#    print "Usage:"
#    print "  ./metos3d compile [MODELNAME...]"
#
## print_usage_update
#def print_usage_update():
#    print "Usage:"
#    print "  ./metos3d update [all | self | data | model | simpack]"
#
## print_usage_help
#def print_usage_help():
#    print "Usage:"
#    print "  ./metos3d help [all | self | data | model | simpack]"







