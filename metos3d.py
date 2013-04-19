#!/usr/bin/env python

global mdir

#
#   print_usage
#
def print_usage():
    print "Usage:"
    print "  ./metos3d update [all | self | data | model | simpack]"
    print "  ./metos3d compile [MODELNAME...]"
#        print "  ./metos3d petsc"
#        print "  ./metos3d help"

#
#   execute_command
#
def execute_command(cmd, msg, errmsg):
    # execute command
    import subprocess
    print "# Executing:", cmd
    proc = subprocess.Popen(cmd, shell=True)
    out  = proc.communicate()
    # check for erro
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

#
#   do_update_self
#
def do_update_self():
    print "# Selfupdate ..."
    # update metos3d
    cmd = "cd " + mdir + "/metos3d/; git pull; cd ../../"
    msg = "# Selfupdate successfully applied."
    errmsg = "Could not update myself."
    if not execute_command(cmd, msg, errmsg) == 0: sys.exit(0)

#
#   do_update_data
#
def do_update_data():
    print "# Updating data ..."
    # update data
    cmd = "cd " + mdir + "/data/; git pull; cd ../../"
    msg = "# Data update successfully applied."
    errmsg = "Could not update data."
    if not execute_command(cmd, msg, errmsg) == 0: sys.exit(0)

#
#   do_update_model
#
def do_update_model():
    print "# Updating model ..."
    # update model
    cmd = "cd " + mdir + "/model/; git pull; cd ../../"
    msg = "# Model update successfully applied."
    errmsg = "Could not update model."
    if not execute_command(cmd, msg, errmsg) == 0: sys.exit(0)

#
#   do_update_simpack
#
def do_update_simpack():
    print "# Updating simpack ..."
    # update simpack
    cmd = "cd " + mdir + "/simpack/; git pull; cd ../../"
    msg = "# Simpack update successfully applied."
    errmsg = "Could not update simpack."
    if not execute_command(cmd, msg, errmsg) == 0: sys.exit(0)

#
#   do_update_all
#
def do_update_all():
    print "# Updating all ..."
    do_update_self()
    do_update_data()
    do_update_model()
    do_update_simpack()
    print "# All packages successfully updated."

#
#   do_update
#
def do_update(argv):
    import sys
    print "# Update ..."
    # dispatch subcommand
    if len(argv) < 3:
        print "# ERROR: No subcommand given."
        print_usage()
        sys.exit(0)
    status = "unknown"
    if argv[2] == "all":
        do_update_all()
        status = "OK"
    if argv[2] == "self":
        do_update_self()
        status = "OK"
    if argv[2] == "data":
        do_update_data()
        status = "OK"
    if argv[2] == "model":
        do_update_model()
        status = "OK"
    if argv[2] == "simpack":
        do_update_simpack()
        status = "OK"
    if status == "unknown":
        print "# ERROR: Unknown subcommand:", argv[2]

#
#   do_model_show
#
def do_model_show():
    print "# Listing available models ..."
    # list models
    cmd = "cat .local/model/official_model_list.txt"
    msg = "# End of list"
    errmsg = "Could not show available models."
    if not execute_command(cmd, msg, errmsg) == 0: sys.exit(0)

#
#   do_compile
#
def do_compile(argv):
    import sys
    print "# Compiling ..."
    # show models
    if len(argv) < 3:
        do_model_show()
        sys.exit(0)
    modelname = argv[2]
    


#
#   dispatch_subcommand
#
def dispatch_subcommand(argv):
    status = "unknown"
    if argv[1] == "update":
        do_update(argv)
        status = "OK"
    if argv[1] == "compile":
        do_compile(argv)
        status = "OK"
    if status == "unknown":
        print "# ERROR: Unknown command:", argv[1]

#
#   main
#
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print_usage()
    else:
        mdir = ".local"
        dispatch_subcommand(sys.argv)
