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
#   Metos3D module
#
import os
import sys
import subprocess

# define local metos3d directory globally
global m3ddir
m3ddir = "local"

########################################################################
### output
########################################################################

# print_error
def print_error(msg):
    print "#"
    print "#   ERROR:", msg
    print "#"

# print_usage
def print_usage():
    print "Usage:"
    print "  ./metos3d compile [MODELNAME...]"
    print "  ./metos3d update  [all | self | data | model | simpack]"
    print "  ./metos3d help    [all | self | data | model | simpack]"

########################################################################
### shell command execution
########################################################################

# execute_command
def execute_command(cmd, msg, errmsg):
    print "# Executing:", cmd
    proc = subprocess.Popen(cmd, shell=True)
    out  = proc.communicate()
    # check for error
    if proc.returncode == 0:
        print msg
        return proc.returncode
    else:
        print "#"
        print "#   Okay, this shouldn't happen ..."
        print "#"
        print "#   The command:", cmd
        print "#   Returned:", proc.returncode
        print "#   We expected: 0, i.e. a success."
        print "#"
        print "#  ", errmsg
        print "#"
        print "#   What now?"
        print "#   1. If you understand, what went wrong, solve the problem and rerun the script."
        print "#   2. If you need help, contact jpi@informatik.uni-kiel.de, attach the output of the script and kindly ask for help."
        print "#"
        return proc.returncode

# execute_commands
def execute_commands(cmds, msg, errmsg):
    print cmds, msg, errmsg

########################################################################
### update
########################################################################

# update_self
def update_self():
    print "# Selfupdate ..."
    # update metos3d
    cmd = "cd " + m3ddir + "/metos3d/; git pull; cd ../../"
    msg = "# Selfupdate successfully applied."
    errmsg = "Could not update myself."
    if not execute_command(cmd, msg, errmsg) == 0: sys.exit(0)

# update_data
def update_data():
    print "# Updating data ..."
    # update data
    cmd = "cd " + m3ddir + "/data/; git pull; cd ../../"
    msg = "# Data update successfully applied."
    errmsg = "Could not update data."
    if not execute_command(cmd, msg, errmsg) == 0: sys.exit(0)

# update_model
def update_model():
    print "# Updating model ..."
    # update model
    cmd = "cd " + m3ddir + "/model/; git pull; cd ../../"
    msg = "# Model update successfully applied."
    errmsg = "Could not update model."
    if not execute_command(cmd, msg, errmsg) == 0: sys.exit(0)

# update_simpack
def update_simpack():
    print "# Updating simpack ..."
    # update simpack
    cmd = "cd " + m3ddir + "/simpack/; git pull; cd ../../"
    msg = "# Simpack update successfully applied."
    errmsg = "Could not update simpack."
    if not execute_command(cmd, msg, errmsg) == 0: sys.exit(0)

# update_all
def update_all():
    print "# Updating all ..."
    update_self()
    update_data()
    update_model()
    update_simpack()
    print "# All packages successfully updated."

########################################################################
### compile
########################################################################

#
#   compile_model_show
#
def compile_model_show():
    print "# Listing available models ..."
    # list models
    cmd = "cat " + m3ddir + "/model/official_model_list.txt"
    msg = "# End of list"
    errmsg = "Could not show available models."
    if not execute_command(cmd, msg, errmsg) == 0: sys.exit(0)

#
#   compile_model
#
def compile_model(modelname):
    print "# MODELNAME:", modelname
    modeldir = m3ddir + "/model/" + modelname
    # no model dir
    if not os.path.exists(modeldir):
        print_error("Model directory does not exist: " + modeldir)
        compile_model_show()
        return "not compiled"
    # compile model
    else:
        cmd = "cd " + m3ddir + "/simpack/; cd ../../"
        msg = "# Successfully compiled " + modelname + " model."
        errmsg = "Could not compile " + modelname + " model."
        if not execute_command(cmd, msg, errmsg) == 0: sys.exit(0)

########################################################################
### help
########################################################################


########################################################################
### subcommand dispatch
########################################################################

# dispatch_update
def dispatch_update(argv):
    print "# Update ..."
    # no subcommand
    if len(argv) < 3:
        print_error("No subcommand given.")
        print_usage()
        return "not updated"
    # all
    status = "unknown"
    if argv[2] == "all":
        status = update_all()
    # self
    if argv[2] == "self":
        status = update_self()
    # data
    if argv[2] == "data":
        status = update_data()
    # model
    if argv[2] == "model":
        status = update_model()
    # simpack
    if argv[2] == "simpack":
        status = update_simpack()
    # unknown
    if status == "unknown":
        print_error("Unknown subcommand: " + argv[2])
        print_usage()
    return status

# dispatch_compile
def dispatch_compile(argv):
    print "# Compile ..."
    # no model name
    if len(argv) < 3:
        print_error("No model name given.")
        print_usage()
        return "not compiled"
    # compile model
    status = compile_model(argv[2])
    return status

# dispatch_help
def dispatch_help(argv):
    print "# Help ..."
    # no subcommand
    if len(argv) < 3:
        print_error("No subcommand given.")
        print_usage()
        return "no help showed"
    # all
    status = "unknown"
    if argv[2] == "all":
        status = help_all()
    # self
    if argv[2] == "self":
        status = help_self()
    # data
    if argv[2] == "data":
        status = help_data()
    # model
    if argv[2] == "model":
        status = help_model()
    # simpack
    if argv[2] == "simpack":
        status = help_simpack()
    # unknown
    if status == "unknown":
        print_error("Unknown subcommand: " + argv[2])
        print_usage()
    return status

########################################################################
### main dispatch
########################################################################

# dispatch_command
def dispatch_command(argv):
    status = "unknown"
    # update
    if argv[1] == "update":
        status = dispatch_update(argv)
    # compile
    if argv[1] == "compile":
        status = dispatch_compile(argv)
    # help
    if argv[1] == "help":
        status = dispatch_help(argv)
    # unknown
    if status == "unknown":
        print_error("Unknown command: " + argv[1])
        print_usage()

    print "# DEBUG: Status:", status















