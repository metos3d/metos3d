#!/usr/bin/env python

import sys
import metos3d_mod as m3d

#
#   main
#
if __name__ == "__main__":
    if len(sys.argv) == 1:
        m3d.print_usage()
    else:
        m3d.dispatch_command(sys.argv)


