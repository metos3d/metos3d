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
    print("### ERROR ###")
    print("### ERROR ###   Okay, this shouldn't happen ...")
    print("### ERROR ###")
    print("### ERROR ###   The command: {}".format(cmd))
    print("### ERROR ###   Returned: {}".format(code))
    print("### ERROR ###   We expected: 0, i.e. a success.")
    print("### ERROR ###")
    print("### ERROR ###   What now?")
    print("### ERROR ###   1. If you understand, what went wrong, solve the problem and rerun the script.")
    print("### ERROR ###   2. If you need help, contact jpi@informatik.uni-kiel.de, attach the output of the script and kindly ask for help.")
    print("### ERROR ###")

# print_usage
def print_usage():
    print("Usage:")
    print("  metos3d [-v] simpack [model-name] [clean]")
    print("  metos3d [-v] matrix [exp|imp] [count] [factor] [file-format-in] [file-format-out]")
    print("  metos3d [-v] update")
    print("  metos3d [-v] info")

# print_usage_matrix
def print_usage_matrix():
    print("Usage:")
    print("  metos3d [-v] matrix [exp|imp] [count] [factor] [file-format-in] [file-format-out]")
    print("Example:")
    print("  # create 4dt matrices")
    print("  cd data/TMM/2.8/Transport/Matrix5_4/")
    print("  mkdir 4dt")
    print("  metos3d matrix exp 12 4 1dt/Ae_%02d.petsc 4dt/Ae_%02d.petsc")
    print("  metos3d matrix imp 12 4 1dt/Ai_%02d.petsc 4dt/Ai_%02d.petsc")

########################################################################
### shell command execution
########################################################################

# execute_command
def execute_command(cmd):
    # execute
    proc = subprocess.Popen(cmd, shell = True)
    out, err  = proc.communicate()
    # check for error
    if not proc.returncode == 0:
        print_execute_fail(cmd, proc.returncode)
        sys.exit(proc.returncode)

# execute_command_pipe
def execute_command_pipe(cmd):
    # execute
    proc = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
    out, err = proc.communicate()
    try:
        out = out.decode('utf-8')
        err = err.decode('utf-8')
    except AttributeError:
        pass
    # check for return code
    if not proc.returncode == 0:
        print_execute_fail(cmd, proc.returncode)
        sys.exit(proc.returncode)
    # check for stderr
    if not err == '':
#        print_error("")
#        print_error("Command execution failed: " + cmd)
#        print_error("")
        print(err)
#        sys.exit(1)
    # stdout and stderr
    return out, err

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
        out, err = execute_command_pipe(cmd)

########################################################################
### compile
########################################################################

# compile_simpack
def compile_simpack(m3dprefix, argv):
    # check PETSc variables
    try:
        petscdir = os.environ["PETSC_DIR"]
        petscarch = os.environ["PETSC_ARCH"]
    except KeyError:
        print_error("PETSc variables are not set.")
        sys.exit(1)
    # get model name
    modelname = argv[2]
    # assemble model path
    modeldir = m3dprefix + "/model/model/" + modelname
    # no model dir
    if not os.path.exists(modeldir):
        print_error("Model directory '" + modeldir + "' does not exist.")
        sys.exit(1)
    else:
        # create links
        # data
        compile_simpack_link("data", m3dprefix + "/data/data")
        # model
        compile_simpack_link("model", m3dprefix + "/model/model")
        # simpack
        compile_simpack_link("simpack", m3dprefix + "/simpack")
        # Makefile
        compile_simpack_link("Makefile", m3dprefix + "/metos3d/Makefile")
        # make clean, if desired
        if len(argv) == 4:
            if argv[3] == "clean":
                # print info
                print("Cleaning '" + modelname + "' model ...")
                # assemble command and execute
                cmd = "make BGC=model/" + modelname + " clean"
                execute_command_debug(cmd)
            else:
                print_error("Unknown command: " + argv[3])
                sys.exit(1)
        else:
            # make work directory
            compile_simpack_mkdir("work")
            # compile simpack and BGC model
            # make BGC
            compile_simpack_make(modelname, argv)

# compile_simpack_make
def compile_simpack_make(modelname, argv):
    # print info
    print("Compiling '" + modelname + "' model ...")
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
### convert matrix
########################################################################

# convert_matrix
def convert_matrix(matrixtype, factor, filepathin, filepathout):
    print("Converting ... '%s' to '%s', type: '%s', factor: %d" % (filepathin, filepathout, matrixtype, factor))
    # check modules
    try:
        import numpy as np
        from scipy.sparse import csr_matrix, eye
    except:
        print_error("No scipy module available. See: https://www.scipy.org/")
        sys.exit(1)
    # read file, first 16 bytes only
    [id, nrow, ncol, nnz] = np.fromfile(filepathin, dtype = '>i4', count = 4)
    # construct the petsc aij data type
    petscaij = '>i4, >i4, >i4, >i4, %d>i4, %d>i4, %d>f8' % (nrow, nnz, nnz)
    # read whole file
    matrixarray = np.fromfile(filepathin, dtype = petscaij)
    # get members of data type
    [id, nrow, ncol, nnz, nnzrow, indices, data] = matrixarray[0]
    # create index set for scipy csr matrix format
    indptr = np.insert(np.cumsum(nnzrow), 0, 0)
    # create matrix
    A = csr_matrix((data, indices, indptr), shape=(nrow, ncol))
    # set factor
    m = factor
    # check matrix type
    if matrixtype == 'exp':
        # create identity
        I = eye(nrow, format = 'csr')
        # compute coarser time step
        Am = I + m * (A - I)
    elif matrixtype == 'imp':
        # compute coarser time step
        Am = A**m
    # prepare for storage, note: we assume the structure did not change
    matrixarray[0][5] = Am.indices
    matrixarray[0][6] = Am.data
    # store matrix
    matrixarray.tofile(filepathout)

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
        # assemble command
        cmd = "ls " + m3dprefix + "/model/model"
        # debug?
        global debug
        if debug:
            # yes, execute and print command
            execute_command_debug(cmd)
        else:
            # no, just execute
            execute_command(cmd)
    else:
        # yes, compile model
        compile_simpack(m3dprefix, argv)

# dispatch_mat
def dispatch_matrix(m3dprefix, argv):
    # check matrix type
    try:
        matrixtype = argv[2]
        # check if type is know
        if not (matrixtype == 'exp' or matrixtype == 'imp'):
            print_error("Matrix type '%s' unknown." % matrixtype)
            print_usage_matrix()
            sys.exit(1)
    except IndexError:
        print_error("No matrix type provided.")
        print_usage_matrix()
        sys.exit(1)
    # check count
    try:
        matrixcount = int(argv[3])
        # check if positive
        if matrixcount < 1:
            print_error("Matrix count '%s' is not positive." % argv[3])
            print_usage_matrix()
            sys.exit(1)
    except IndexError:
        print_error("No matrix count provided.")
        print_usage_matrix()
        sys.exit(1)
    except ValueError:
        print_error("Matrix count '%s' is not an integer." % argv[3])
        print_usage_matrix()
        sys.exit(1)
    # check factor
    try:
        factor = int(argv[4])
        # check if positive
        if factor < 1:
            print_error("Factor '%s' is not positive." % argv[4])
            print_usage_matrix()
            sys.exit(1)
    except IndexError:
        print_error("No factor provided.")
        print_usage_matrix()
        sys.exit(1)
    except ValueError:
        print_error("Factor count '%s' is not an integer." % argv[4])
        print_usage_matrix()
        sys.exit(1)
    # check input file format
    try:
        fileformatin = argv[5]
    except:
        print_error("No input file format provided.")
        print_usage_matrix()
        sys.exit(1)
    # check output file format
    try:
        fileformatout = argv[6]
    except:
        print_error("No output file format provided.")
        print_usage_matrix()
        sys.exit(1)
    # convert matrices
    for imat in range(matrixcount):
        # construct file paths
        filepathin = fileformatin % imat
        filepathout = fileformatout % imat
        # convert matrix
        convert_matrix(matrixtype, factor, filepathin, filepathout)

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
#    cmd = "cd " + m3dprefix + "/" + repository + "/; git checkout master; git pull --tag"
    cmd = "cd " + m3dprefix + "/" + repository + "/; git pull --tag"
    execute_command_debug(cmd)

# dispatch_info
def dispatch_info(m3dprefix, argv):
    # provide information about the repository versions
    print("Your are using the following tags and branches of the Metos3D repositories:")
    print("")
    print("  %-10s%-20s%s" % ("name", "tag", "branch"))
    print("  %-10s%-20s%s" % ("----", "---", "------"))
    # metos3d
    dispatch_info_repository(m3dprefix, "metos3d")
    # simpack
    dispatch_info_repository(m3dprefix, "simpack")
    # model
    dispatch_info_repository(m3dprefix, "model")
    # data
    dispatch_info_repository(m3dprefix, "data")
    print("")

# dispatch_info_repository
def dispatch_info_repository(m3dprefix, repository):
    # prepare command, execute and provide information
    # tags
    cmd = "cd " + m3dprefix + "/" + repository + "/; git describe --always"
    # debug?
    global debug
    if debug:
        # yes, print shell command additionally
        print_debug("Executing: " + cmd)
    # execute
    outtag, err = execute_command_pipe(cmd)
    outtag = outtag.rstrip()
    # branches
    cmd = "cd " + m3dprefix + "/" + repository + "/; git symbolic-ref --short HEAD"
    # debug?
    if debug:
        # yes, print shell command additionally
        print_debug("Executing: " + cmd)
    # execute
    outbranch, err = execute_command_pipe(cmd)
    outbranch = outbranch.rstrip()
    # repo info
    print("  %-10s%-20s%s" % (repository, outtag, outbranch))

########################################################################
### main dispatch
########################################################################

# dispatch_command
def dispatch_command(m3dprefix, argv):
    # print(m3dprefix)
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
    # mat
    elif argv[1] == "matrix":
        dispatch_matrix(m3dprefix, argv)
    # update
    elif argv[1] == "update":
        dispatch_update(m3dprefix, argv)
    # info
    elif argv[1] == "info":
        dispatch_info(m3dprefix, argv)
    # unknown
    else:
        print_error("Unknown option or command: " + argv[1])
