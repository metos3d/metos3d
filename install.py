#!/usr/bin/env python
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

import os
import sys
import subprocess

########################################################################
### shell command execution
########################################################################

# execute_command
def execute_command(cmd):
    print("#     Executing: " + cmd)
    proc = subprocess.Popen(cmd, shell = True)
    out = proc.communicate()
    # check for error
    if not proc.returncode == 0:
        print("")
        print("### ERROR ###")
        print("### ERROR ###   Okay, this shouldn't happen ...")
        print("### ERROR ###")
        print("### ERROR ###   The command: {}".format(cmd))
        print("### ERROR ###   Returned: {}".format(proc.returncode))
        print("### ERROR ###   We expected: 0, i.e. a success.")
        print("### ERROR ###")
        print("### ERROR ###   What now?")
        print("### ERROR ###   1. If you understand, what went wrong, solve the problem and rerun the script.")
        print("### ERROR ###   2. If you need help, you may contact ts@informatik.uni-kiel.de")
        sys.exit(proc.returncode)

########################################################################
### interaction with user
########################################################################

# get_user_input
def get_user_input(question, default_answer):
    # workaround for different python versions
    try:
        # python 2
        answer = raw_input(question) or default_answer
    except NameError:
        # python 3
        answer = input(question) or default_answer
    # return
    return answer

########################################################################
### subroutines
########################################################################

# create_installation_directory
def create_installation_directory(m3dprefix):
    # question and default answer
    question = "Create installation directory '" + m3dprefix + "'? [yes]/no \n>>> "
    default_answer = "yes"
    # ask user
    answer = get_user_input(question, default_answer)
    # proceed accordingly
    if answer != "yes":
        return
    else:
        # create install folder
        print("#")
        print("#   Creating installation directory '" + m3dprefix + "'.")
        cmd = "mkdir " + m3dprefix
        execute_command(cmd)
        print("#   Directory '" + m3dprefix + "' successfully created.")
        print("#")

# clone_repository
def clone_repository(m3dprefix, name):
    # question and default answer
    question = "Clone '" + name + "' repository into '" + m3dprefix + "'? [yes]/no \n>>> "
    default_answer = "yes"
    # ask user
    answer = get_user_input(question, default_answer)
    # proceed accordingly
    if answer != "yes":
        return
    else:
        # clone
        print("#")
        print("#   Cloning git repository '" + name + "'.")
        cmd = "cd " + m3dprefix + "; git clone https://github.com/metos3d/" + name + ".git"
        execute_command(cmd)
        print("#   Repository '" + name + "' successfully cloned.")
        print("#")

# clone_repository_data
def clone_repository_data(m3dprefix):
    # repository
    name = "data"
    # question and default answer
    question = "Clone '" + name + "' repository into '" + m3dprefix + "'? [yes]/no \n>>> "
    default_answer = "yes"
    # ask user
    answer = get_user_input(question, default_answer)
    # proceed accordingly
    if answer != "yes":
        return
    else:
        # clone
        print("#")
        print("#   Cloning git repository '" + name + "'.")
        cmd = "cd " + m3dprefix + "; git clone https://github.com/metos3d/" + name + ".git"
        execute_command(cmd)
        print("#   Repository '" + name + "' successfully cloned.")
        print("#")
        # extract data
        print("#")
        print("#   Extracting data.")
        execute_command("cd " + m3dprefix + "/data/data; gunzip -c TMM.tar.gz > TMM.tar")
        execute_command("cd " + m3dprefix + "/data/data; tar xf TMM.tar")
        execute_command("cd " + m3dprefix + "/data/data; rm -f TMM.tar")
        print("#   Data successfully extracted.")
        print("#")

########################################################################
### main
########################################################################

# main
if __name__ == "__main__":
    # say hello
    print("#")
    print("#   Metos3D: Marine Ecosystem Toolkit for Optimization and Simulation in 3-D")
    print("#     Install script")
    print("#")
    # show steps
    print("#   The installation consists of the following steps:")
    print("#     1. Create installation directory'")
    print("#     2. Clone the 'metos3d', 'simpack', 'model' and 'data' git repositories into the installation directory")
    print("#")
    print("#     Afterwards, you have to define/(modify) two environment/shell variables:")
    print("#     1. Define a new one named 'METOS3D_DIR' pointing to the installation directory.")
    print("#     2. Modify your 'PATH' variable to include the '$METOS3D_DIR/metos3d' subdirectory.")
    print("#")
    # ask for installation directory (m3dprefix)
    default_answer = ".metos3d"
    question = "Define installation directory (must not exist, path relative path to home directory) [default: ~/" + default_answer + "]\n>>> "
    # ask user
    answer = get_user_input(question, default_answer)
    m3dprefix = os.path.expanduser("~/" + answer)
    ###
    ### 1. Create installation directory:
    ###
    # directory
    create_installation_directory(m3dprefix)
    ###
    ### 2. Clone the 'metos3d', 'simpack', 'model' and 'data' git repositories into '~/.metos3d'.
    ###
    # repositories
    clone_repository(m3dprefix, "metos3d")
    clone_repository(m3dprefix, "simpack")
    clone_repository(m3dprefix, "model")
    clone_repository_data(m3dprefix)
    # success
    print("#")
    print("#   Now, define a new environment/shell variable named 'METOS3D_DIR'")
    print("#   pointing to the installation directory" + m3dprefix)
    print("#   and add '" + m3dprefix + "/metos3d' to the search path of your shell.")
    print("#   This means, include")
    print("#")
    print("#   export METOS3D_DIR=" + m3dprefix)
    print("#   export PATH=" + m3dprefix + "/metos3d:$PATH")
    print("#")
    print("#   in your shell config file ('~/.bashrc' or '~/.bash_profile' for example).")
    print("#   You can run Metos3D as a usual shell command then:")
    print("#")
    print("#   $> metos3d")
    print("#   Usage:")
    print("#     metos3d [-v] simpack [model-name] [clean]")
    print("#     metos3d [-v] matrix [exp|imp] [count] [factor] [file-format-in] [file-format-out]")
    print("#     metos3d [-v] update")
    print("#     metos3d [-v] info")
    print("#")
    print("#   You may also have to set the PETSC_ARCH and PETSC_DIR shell variables.")
    print("#")
    # example
    print("#   As a simple example, execute:")
    print("#")
    print("#   $> metos3d simpack N")
    print("#")
    print("#   This will:")
    print("#   1. In the current directory, generate links \"data, model, simpack\" ")
    print("#      pointing to the corresponding subdirectories in the installation directory " + m3dprefix)
    print("#   2. compile the code for one model")
    print("#")
    print("#   $> ./metos3d-simpack-N.exe model/N/option/test.N.option.txt")
    print("#   This will run the model for a short test.")
    print("#")
