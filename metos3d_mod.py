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
import re
import os
import sys
import subprocess

########################################################################
### output
########################################################################

# print_error
def print_error(msg):
    print "### ERROR: " + msg

# print_execute_fail
def print_execute_fail(cmd, code):
    print "#"
    print "#   Okay, this shouldn't happen ..."
    print "#"
    print "#   The command:", cmd
    print "#   Returned:", code
    print "#   We expected: 0, i.e. a success."
    print "#"
    print "#   What now?"
    print "#   1. If you understand, what went wrong, solve the problem and rerun the script."
    print "#   2. If you need help, contact jpi@informatik.uni-kiel.de, attach the output of the script and kindly ask for help."
    print "#"

# print_usage
def print_usage():
    print "Usage:"
    print "  metos3d simpack [MODELNAME...]"
    print "  metos3d petsc   [VERSION...]"
    print "  metos3d update"

########################################################################
### shell command execution
########################################################################

# execute_command
def execute_command(cmd):
    print "### EXECUTING: " + cmd
    # execute
    proc = subprocess.Popen(cmd, shell = True)
    out  = proc.communicate()
    # check for error
    if not proc.returncode == 0:
        print_execute_fail(cmd, proc.returncode)
        sys.exit(proc.returncode)

# execute_command_safe
def execute_command_safe(token, cmd):
    if not os.path.exists(token):
        execute_command(cmd)

# execute_petsc_configure
def execute_petsc_configure(cmd):
    print "### EXECUTING: " + cmd
    # execute
    proc = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    out  = proc.communicate()
    # check for error
    if not proc.returncode == 0:
        print_execute_fail(cmd, proc.returncode)
        sys.exit(proc.returncode)
    else:
        for line in out[0].split("\n"):
            match = re.search("^  PETSC_ARCH: (.+)", line)
            if match: petscarch = match.groups()[0]
            match = re.search("^  PETSC_DIR: (.+)", line)
            if match: petscdir = match.groups()[0]
    # return variables
    return (petscarch, petscdir)

########################################################################
### compile
########################################################################

# compile_simpack
def compile_simpack(m3dprefix, modelname):
    modeldir = m3dprefix + "/model/model/" + modelname
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
        execute_command_safe("data", "ln -s " + m3dprefix + "/data/data")
        # model
        execute_command_safe("model", "ln -s " + m3dprefix + "/model/model")
        # simpack
        execute_command_safe("simpack", "ln -s " + m3dprefix + "/simpack")
        # Makefile
        execute_command_safe("Makefile", "ln -s " + m3dprefix + "/metos3d/Makefile")
        # make clean
        execute_command("make BGC=model/" + modelname + " clean")
        # make
        execute_command("make BGC=model/" + modelname)
        # work
        execute_command_safe("work", "mkdir work")

# compile petsc
def compile_petsc(m3dprefix, petscversion):
    # create petsc dir
    petscprefix = m3dprefix + "/petsc"
    execute_command_safe(petscprefix, "mkdir " + petscprefix)
    # download petsc
    execute_command("cd " + petscprefix + "; curl -O ftp://ftp.mcs.anl.gov/pub/petsc/release-snapshots/" + petscversion)
    # unzip
    execute_command("cd " + petscprefix + "; gunzip " + petscversion)
    # untar
    petscversion = petscversion.replace(".gz", "")
    execute_command("cd " + petscprefix + "; tar xf " + petscversion)
    # configure
    petscversion = petscversion.replace(".tar", "")
    petscversion = petscversion.replace("-lite-", "-")
    petscversionprefix = petscprefix + "/" + petscversion
    (petscarch, petscdir) = execute_petsc_configure("cd " + petscversionprefix + "; ./configure")
    # make
    execute_command("cd " + petscversionprefix + "; make PETSC_DIR=" + petscdir + " PETSC_ARCH=" + petscarch + " all")
    # info
    print "#"
    print "#   Now, add the PETSc variables permanently to your shell environment."
    print "#   Or just copy the following lines and paste them into your shell:"
    print "#"
    print "export PETSC_DIR=" + petscdir
    print "export PETSC_ARCH=" + petscarch

########################################################################
### subcommand dispatch
########################################################################

# dispatch_simpack
def dispatch_simpack(m3dprefix, argv):
    # no model
    if len(argv) < 3:
        execute_command("ls " + m3dprefix + "/model/model");
    # compile
    else:
        compile_simpack(m3dprefix, argv[2])

# dispatch_update
def dispatch_update(m3dprefix, argv):
    # metos3d
    execute_command("cd " + m3dprefix + "/metos3d/; git checkout master; git pull")
    # data
    execute_command("cd " + m3dprefix + "/data/; git checkout master; git pull")
    # model
    execute_command("cd " + m3dprefix + "/model/; git checkout master; git pull")
    # simpack
    execute_command("cd " + m3dprefix + "/simpack/; git checkout master; git pull")

# dispatch_petsc
def dispatch_petsc(m3dprefix, argv):
    # check PETSc variables
    try:
        petscdir = os.environ["PETSC_DIR"]
        petscarch = os.environ["PETSC_ARCH"]
        # already set
        print_error("PETSc variables are already set: PETSC_DIR=" + petscdir + " PETSC_ARCH=" + petscarch)
        print_error("Unset them to proceed: unset PETSC_DIR; unset PETSC_ARCH;")
    except KeyError:
        # no version
        if len(argv) < 3:
            execute_command("curl -sl ftp://ftp.mcs.anl.gov/pub/petsc/release-snapshots/ | grep 'petsc-lite-3.3-' | sort");
        else:
            compile_petsc(m3dprefix, argv[2])

########################################################################
### main dispatch
########################################################################

# dispatch_command
def dispatch_command(m3dprefix, argv):
    # simpack
    if argv[1] == "simpack":
        dispatch_simpack(m3dprefix, argv)
    # update
    elif argv[1] == "update":
        dispatch_update(m3dprefix, argv)
    # petsc
    elif argv[1] == "petsc":
        dispatch_petsc(m3dprefix, argv)
    # unknown
    else:
        print_error("Unknown command: " + argv[1])






