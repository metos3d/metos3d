#!/usr/bin/env python

#
#   execute_command
#
def execute_command(cmd, msg, errmsg):
    # execute command
    import subprocess
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
#   do_compile_model
#
def do_compile_model(modelname):
    import os
    import sys
    print "# MODELNAME:", modelname
    dirpath = mdir + "/model/" + modelname
    if not os.path.exists(dirpath):
        print "# ERROR: Model directory does not exist."
        do_model_show()
        sys.exit(0)
    else:
        # compile model
        cmd = "cd " + mdir + "/simpack/; cd ../../"
        msg = "# Successfully compiled " + modelname + " model."
        errmsg = "Could not compile " + modelname + " model."
        if not execute_command(cmd, msg, errmsg) == 0: sys.exit(0)

#
#   do_compile
#
def do_compile(argv):
    import sys
    print "# Compile ..."
    # show models
    if len(argv) < 3:
        print "# ERROR: No MODELNAME given."
        do_model_show()
        sys.exit(0)
    else:
        do_compile_model(argv[2])

#
#   main
#
if __name__ == "__main__":
    import sys
    import metos3d_util as m3d
    if len(sys.argv) == 1:
        m3d.print_usage()
    else:
        m3d.dispatch_subcommand(sys.argv)


