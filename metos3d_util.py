#
#   Metos3D Utilities Module
#

#
#   define local metos3d directory globally
#
global mdir
mdir = "local"

#
#   print_usage
#
def print_usage():
    print "Usage:"
    print "  ./metos3d update [all | self | data | model | simpack]"
    print "  ./metos3d compile [MODELNAME...]"

#
#   do_update
#
def do_update(argv):
    import sys
    print "# Update ..."
    # dispatch subcommand
    # no subcommand
    if len(argv) < 3:
        print "# ERROR: No subcommand given."
        print_usage()
        sys.exit(0)
    # 
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
