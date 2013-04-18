#!/usr/bin/env python

global mdir

#
#   execute_command
#
def execute_command(cmd, msg):
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
#   do_selfupdate
#
def do_selfupdate():
    print "# Updating Metos3D ..."
    # update metos3d
    cmd = "cd " + mdir + "/metos3d/; git pull; cd ../../"
    msg = "# Updated metos3d script"
    errmsg = "Could not update metos3d script."
    if not execute_command(cmd, msg) == 0: sys.exit(0)

#
#   dispatch_subcommand
#
def dispatch_subcommand(argv):
    if argv[1] == "selfupdate":
        do_selfupdate()
    else:
        print "# ERROR: Unknown command:", argv[1]

#
#   main
#
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print "Example usage:"
        print "  ./metos3d selfupdate"
#        print "  ./metos3d data"
#        print "  ./metos3d model"
#        print "  ./metos3d simpack"
#        print "  ./metos3d petsc"
#        print "  ./metos3d help"
    else:
        mdir = ".local"
        dispatch_subcommand(sys.argv)
