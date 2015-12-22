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

# debug
debug = False

########################################################################
### output
########################################################################

# print_debug
def print_debug(msg):
    # debug?
    global debug
    if debug:
        # yes, print message
        print("### DEBUG ### " + msg)

# print_error
def print_error(msg):
    print("### ERROR ### " + msg)

# print_execute_fail
def print_execute_fail(cmd, code):
    print "### ERROR ###"
    print "### ERROR ###   Okay, this shouldn't happen ..."
    print "### ERROR ###"
    print "### ERROR ###   The command:", cmd
    print "### ERROR ###   Returned:", code
    print "### ERROR ###   We expected: 0, i.e. a success."
    print "### ERROR ###"
    print "### ERROR ###   What now?"
    print "### ERROR ###   1. If you understand, what went wrong, solve the problem and rerun the script."
    print "### ERROR ###   2. If you need help, contact jpi@informatik.uni-kiel.de, attach the output of the script and kindly ask for help."
    print "### ERROR ###"

# print_usage
def print_usage():
    print("Usage:")
    print("  metos3d [-v] simpack [MODELNAME...]")
    print("  metos3d [-v] update")
    print("  metos3d [-v] info")
    print("  metos3d help")

# print_help
def print_help():
    print("Help:")
    print("  Compiling and linking a model:")
    print("  PETSc variables:")

########################################################################
### shell command execution
########################################################################

# execute_command
def execute_command(cmd):
    # execute
    proc = subprocess.Popen(cmd, shell = True)
    out  = proc.communicate()
    # check for error
    if not proc.returncode == 0:
        print_execute_fail(cmd, proc.returncode)
        sys.exit(proc.returncode)

# execute_command_pipe
def execute_command_pipe(cmd):
    # execute
    proc = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
    [out, err] = proc.communicate()
    # check for error
    if not proc.returncode == 0:
        print_execute_fail(cmd, proc.returncode)
        sys.exit(proc.returncode)
    # stdout and stderr
    return [out, err]

# execute_command_debug:
def execute_command_debug(cmd):
    # debug?
    global debug
    if debug:
        # yes, print command and execute verbosely
        print_debug("Executing: " + cmd)
        execute_command(cmd)
    else:
        # no, execute quietly
        out = execute_command_pipe(cmd)

########################################################################
### compile
########################################################################

# compile_simpack
def compile_simpack(m3dprefix, modelname):
    # assemble model path
    modeldir = m3dprefix + "/model/model/" + modelname
    # no model dir
    if not os.path.exists(modeldir):
        print_error("Model directory '" + modeldir + "' does not exist.")
        sys.exit(1)
    # compile model
    else:
        # check PETSc variables
        try:
            petscdir = os.environ["PETSC_DIR"]
            petscarch = os.environ["PETSC_ARCH"]
        except KeyError:
            print_error("PETSc variables are not set. See 'metos3d help' for more.")
            sys.exit(1)
        # create links
        # data
        compile_simpack_link("data", m3dprefix + "/data/data")
        # model
        compile_simpack_link("model", m3dprefix + "/model/model")
        # simpack
        compile_simpack_link("simpack", m3dprefix + "/simpack")
        # Makefile
        compile_simpack_link("Makefile", m3dprefix + "/metos3d/Makefile")
        # make directory
        # work
        compile_simpack_mkdir("work")
        # make BGC
        compile_simpack_make(modelname)

# compile_simpack_make
def compile_simpack_make(modelname):
    # print info
    print("Compiling '" + modelname + "' model ...")
    # make clean
    # assemble command and execute
    cmd = "make BGC=model/" + modelname + " clean"
    execute_command_debug(cmd)
    # make
    # assemble command and execute
    cmd = "make BGC=model/" + modelname
    execute_command_debug(cmd)

# compile_simpack_mkdir
def compile_simpack_mkdir(dirname):
    # directory exists?
    if not os.path.exists(dirname):
        # no, make dir
        # print info
        print("Creating directory '" + dirname + "' ...")
        # assemble command and execute
        cmd = "mkdir " + dirname
        execute_command_debug(cmd)
    else:
        # yes, print info if debug
        print_debug("Directory '" + dirname + "' already exists.")

# compile_simpack_link
def compile_simpack_link(linkname, linkpath):
    # link exists?
    if not os.path.exists(linkname):
        # no, create link
        # print info
        print("Creating link '" + linkname + "' ...")
        # assemble command and execute
        cmd = "ln -s " + linkpath
        execute_command_debug(cmd)
    else:
        # yes, print info if debug
        print_debug("Link '" + linkname + "' already exists.")

########################################################################
### subcommand dispatch
########################################################################

# dispatch_simpack
def dispatch_simpack(m3dprefix, argv):
    # model name provided?
    if len(argv) < 3:
        # no, list models
        # print info
        print("Listing avaible models from the 'model' repository ...")
        # assemble command and execute
        cmd = "ls " + m3dprefix + "/model/model"
        execute_command_debug(cmd)
    else:
        # yes, compile model
        compile_simpack(m3dprefix, argv[2])

# dispatch_update
def dispatch_update(m3dprefix, argv):
    # metos3d
    dispatch_update_repository(m3dprefix, "metos3d")
    # data
    dispatch_update_repository(m3dprefix, "data")
    # model
    dispatch_update_repository(m3dprefix, "model")
    # simpack
    dispatch_update_repository(m3dprefix, "simpack")

# dispatch_update_repository(m3dprefix, repository)
def dispatch_update_repository(m3dprefix, repository):
    # print information
    print("Updating '" + repository + "' repository ...")
    # assemble command and execute
    cmd = "cd " + m3dprefix + "/" + repository + "/; git checkout master; git pull"
    execute_command_debug(cmd)

# dispatch_info
def dispatch_info(m3dprefix, argv):
    # provide information about the repository versions
    print("Your are using the following versions of the Metos3D repositories:")
    # metos3d
    dispatch_info_repository(m3dprefix, "metos3d")
    # data
    dispatch_info_repository(m3dprefix, "data")
    # model
    dispatch_info_repository(m3dprefix, "model")
    # simpack
    dispatch_info_repository(m3dprefix, "simpack")

# dispatch_info_repository
def dispatch_info_repository(m3dprefix, repository):
    # prepare command, execute and provide information
    cmd = "cd " + m3dprefix + "/" + repository + "/; git describe --always"
    out = execute_command_pipe(cmd)
    print("  %-10s%-20s") % (repository, out[0].rstrip()),
    # debug?
    global debug
    if debug:
        # yes, print shell command additionally
        print_debug("Executing: " + cmd)
    else:
        # no, just end line
        print("")

# dispatch_help
def dispatch_help(m3dprefix, argv):
    print_help()

########################################################################
### main dispatch
########################################################################

# dispatch_command
def dispatch_command(m3dprefix, argv):
    # no arguments?
    # print usage and exit with code 1
    if len(sys.argv) == 1:
        print_usage()
        sys.exit(1)
    
    # should debug information be provided?
    # use global variable
    global debug
    if "-v" in argv:
        # turn on debugging
        debug = True
        # remove '-v' from the argument list
        argv.remove("-v")

    # command provided?
    if len(argv) == 1:
        # no, print error message and exit with code 1
        print_error("Missing a command.")
        sys.exit(1)

    # simpack
    if argv[1] == "simpack":
        dispatch_simpack(m3dprefix, argv)
    # update
    elif argv[1] == "update":
        dispatch_update(m3dprefix, argv)
    # info
    elif argv[1] == "info":
        dispatch_info(m3dprefix, argv)
    # help
    elif argv[1] == "help":
        dispatch_help(m3dprefix, argv)
    # unknown
    else:
        print_error("Unknown option or command: " + argv[1])









