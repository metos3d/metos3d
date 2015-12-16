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
    print("  metos3d simpack [MODELNAME...] [-v]")
    print("  metos3d update [-v]")
    print("  metos3d info [-v]")
    print("  metos3d help")
#    print("Usage:")
#    print("  metos3d [-v] simpack [MODELNAME...]")
#    print("  metos3d [-v] update")
#    print("  metos3d help")

# print_petsc
def print_petsc():
    print("PETSc:")
    print("  Metos3D ...")
#    print("  metos3d [-v] update")
#    print("  metos3d help")

# print_help
def print_help():
    print("Help:")
    print("  PETSc:")
    print("  Models:")

########################################################################
### shell command execution
########################################################################

# execute_command
def execute_command(cmd):
    print_debug("Executing: " + cmd)
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

# execute_command_safe
def execute_command_safe(token, cmd):
    if not os.path.exists(token):
        execute_command(cmd)

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
            print_error("PETSc variables are not set. See 'metos3d help' for more.")
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

########################################################################
### subcommand dispatch
########################################################################

# dispatch_simpack
def dispatch_simpack(m3dprefix, argv):
    
    print argv
    argv.remove("-v")
    print argv
    
    # no model
    if len(argv) < 3:
#        print_info("Listing all available models.")
        execute_command("ls " + m3dprefix + "/model/model");
    # compile
    else:
        compile_simpack(m3dprefix, argv[2])

# dispatch_update
def dispatch_update(m3dprefix, argv):
    # metos3d
#    print_info("Updating 'metos3d' repository ...")
    execute_command("cd " + m3dprefix + "/metos3d/; git checkout -q master; git pull -q")
    # data
#    print_info("Updating 'data' repository ...")
    execute_command("cd " + m3dprefix + "/data/; git checkout -q master; git pull -q")
    # model
#    execute_command("cd " + m3dprefix + "/model/; git checkout master; git pull")
    [out, err] = execute_command_pipe("cd " + m3dprefix + "/model/; git checkout -q master; git pull -q")
#    print "out:", out
#    print "err:", err
    # simpack
#    execute_command("cd " + m3dprefix + "/simpack/; git checkout master; git pull")

# dispatch_help
def dispatch_help(m3dprefix, argv):
    print_help()
    print "Info:"
    print "  Currently, your are running the following versions of Metos3D repositories:"
    # metos3d
    cmd = "cd " + m3dprefix + "/metos3d/; git describe"
    out = execute_command_pipe(cmd)
    print "    metos3d  %-20s (### EXECUTED: %s)" % (out[0].rstrip(), cmd)
    # data
    cmd = "cd " + m3dprefix + "/data/; git describe"
    out = execute_command_pipe(cmd)
    print "    data     %-20s (### EXECUTED: %s)" % (out[0].rstrip(), cmd)
    # model
    cmd = "cd " + m3dprefix + "/model/; git describe"
    out = execute_command_pipe(cmd)
    print "    model    %-20s (### EXECUTED: %s)" % (out[0].rstrip(), cmd)
    # simpack
    cmd = "cd " + m3dprefix + "/simpack/; git describe"
    out = execute_command_pipe(cmd)
    print "    simpack  %-20s (### EXECUTED: %s)" % (out[0].rstrip(), cmd)

########################################################################
### main dispatch
########################################################################

# dispatch_command
def dispatch_command(m3dprefix, argv):
    # debug
    global debug
    if "-v" in argv:
        debug  = True
        argv.remove("-v")
    
    print debug
    
    # simpack
    if argv[1] == "simpack":
        dispatch_simpack(m3dprefix, argv)
    # update
    elif argv[1] == "update":
        dispatch_update(m3dprefix, argv)
    # help
    elif argv[1] == "help":
        dispatch_help(m3dprefix, argv)
    # unknown
    else:
        print_error("Unknown command: " + argv[1])

#sys.exit(proc.returncode)





