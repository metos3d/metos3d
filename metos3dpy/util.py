#
# Metos3D: A Marine Ecosystem Toolkit for Optimization and Simulation in 3-D
# Copyright (C) 2018  Jaroslaw Piwonski, CAU, jpi@informatik.uni-kiel.de
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

#import os
#import sys
#import socket

from __future__ import print_function

def print_format(message, *extr_args):
    message = message + " "
    print("{:.<40}".format(message), *extr_args)

#def check_hostname(ctx):
#    fqdn = socket.getfqdn()
#    ctx.obj.fqdn = fqdn
#    print_format(ctx, "Checking hostname", fqdn)
#
#def check_directory(ctx):
#    cwd = os.getcwd()
#    ctx.obj.cwd = cwd
#    print_format(ctx, "Checking directory", cwd)
#
#def check_config_file(ctx):
#    file = "metos3d.conf.yaml"
#    print_format(ctx, "Checking config file", file)
#    if not os.path.exists(file):
#        print("no configuration file found ...")
#        sys.exit(1)

