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

import re
import os
import glob
import yaml
import click
import socket
import metos3d
import subprocess

def info(ctx):

    metos3d_conf_file_path = ctx.obj.basepath + "/metos3d.conf.yaml"
    metos3d.debug(ctx, "Checking configuration file", metos3d_conf_file_path)

    try:    metos3d_conf_file = open(metos3d_conf_file_path)
    except: metos3d.error(True, "Can't open configuration file")

    try:    metos3d_conf = yaml.load(metos3d_conf_file)
    except: metos3d.error(True, "Can't load configuration as YAML file")

    try:
        print("Metos3D version ...", metos3d_conf["metos3d"]["version"])
        print("Metos3D environment ...", metos3d_conf["metos3d"]["env"])
        print("PETSc library ...", metos3d_conf["metos3d"]["petsc"])
        print("Metos3D data ...", metos3d_conf["metos3d"]["data"])
        print("Metos3D model ...", metos3d_conf["metos3d"]["model"])
    except:
        metos3d.error(True, "Can't access configuration")


#    if metos3d_conf["metos3d"]["version"] is None:
#        print("version is not set ...")
#        print("Setting version ...", metos3d.__version__)
#        metos3d_conf["metos3d"]["version"] = metos3d.__version__
#
#        with open(metos3d_conf_file, "w") as f:
#            f.write(yaml.dump(metos3d_conf, default_flow_style=False))
#    else:
#
#    if metos3d_conf["metos3d"]["env"] is None:
#        print("env is not set ...")
#
#        host = socket.getfqdn()
#        host_part = host.split(".")
#        host_part.reverse()
#        print("host ...", host, host_part)
#
#        hosts = glob.glob(ctx.obj.basepath + "/env/*")
#        hosts_file = list(map(os.path.basename, hosts))
#        for file in hosts_file:
#            print("hosts ...", file, file.split("."))
#
#    else:
#
#    if metos3d_conf["metos3d"]["petsc"] is None:
#        print("petsc is not set ...")
#
#    if metos3d_conf["metos3d"]["data"] is None:
#        print("data is not set ...")
#
#    if metos3d_conf["metos3d"]["model"] is None:
#        print("model is not set ...")



#    ctx.item_list = [
#                     ["environment.+metos3d-petsc-python2",             "Creating environment"],
#                     ["Configuring PETSc to compile on your system",    "Configuring PETSc"],
#                     ["download.+YAML",                                 "Downloading YAML"],
#                     ["Running configure on YAML",                      "Configuring YAML"],
#                     ["Running make on YAML",                           "Compiling YAML"],
#                     ["Running make install on YAML",                   "Installing YAML"],
#                     ["TESTING:",                                       "Configuring PETSc"],
#                     ["download.+HDF5",                                 "Downloading HDF5"],
#                     ["Running configure on HDF5",                      "Configuring HDF5"],
#                     ["Running make on HDF5",                           "Compiling HDF5"],
#                     ["Running make install on HDF5",                   "Installing HDF5"],
#                     ["TESTING:",                                       "Configuring PETSc"],
#                     ["download.+FBLASLAPACK",                          "Downloading FBLASLAPACK"],
#                     ["Compiling FBLASLAPACK",                          "Compiling FBLASLAPACK"],
#                     ["TESTING:",                                       "Configuring PETSc"],
#                     ["make PETSC_DIR=.+PETSC_ARCH=",                   "Compiling PETSc"],
#                     ["environment.+metos3d-petsc-python2",             "Removing environment"],
#                     ]
#    ctx.item = "Starting"
#
#    # set compiler variables, CC, CXX,FC
##    cmd_env = "source " + ctx.obj.basepath + "/env/generic.mpich.gcc.env.sh"
##    cmd_env = "source " + ctx.obj.basepath + "/env/de.dkrz.mistral.intelmpi.env.sh"
#    cmd_env = "source " + ctx.obj.basepath + "/env/de.uni-kiel.rz.rzcluster.env.sh"
#    cmd_petsc = "source " + ctx.obj.basepath + "/petsc/petsc.conf.sh"
#    cmd = cmd_env + ";" + cmd_petsc
#    proc = subprocess.Popen(cmd,
#                            shell=True,
#                            stdout=subprocess.PIPE,
#                            stderr=subprocess.STDOUT)
#
#    # test on dkrz
#    # time . ../../metos3d/petsc/petsc.conf.sh > petsc_configure_lines.txt &
#    # wc petsc_configure_lines.txt
#    # 2146   5626 176734 petsc_configure_lines.txt
#    with click.progressbar(length=2200,
#                           width=0,
#                           label="metos3d init",
#                           ) as bar:
#
#        pattern = ctx.item_list.pop(0)
#        for item in bar:
#            out = proc.stdout.readline().decode("utf-8")
##            print(out.strip())
#            m = re.search(pattern[0], out) if pattern else None
#            if m:
#                bar.label = pattern[1]
#                pattern = ctx.item_list.pop(0) if ctx.item_list else None













#    proc = subprocess.Popen(["make"], stdout=subprocess.PIPE)
#    with click.progressbar(length=80, width=0, label=proc.args[0], ) as bar:

#    print(proc.returncode)

#    if proc.returncode == 0
#    import time
#    while True:
##        time.sleep(0.05)
#        out = proc.stdout.readline()
##        out = proc.stdout.read(10)
#        if out.decode("ASCII") == "":
#            break
#        print(out)

#    with click.progressbar(length=100, width=0, label="Configure PETSc", ) as bar:
#        for item in bar:
##            print(type(item))
##            print(item)
#            if item > 50:
#                break
#            time.sleep(0.05)

#    if os.path.exists(metos3d_conf_file):
#        info_show_configuration(ctx)
#    else:
#        info_show_message(ctx)

#    import time
#    items = range(400)

#    with click.progressbar(items) as bar:
#        for item in bar:
#            time.sleep(0.05)

#    def my_func(item):
#        return str(item)
##        print(item, end='')

#    import subprocess
##    proc = subprocess.Popen(["make", "clean"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=0)
#    proc = subprocess.Popen(["make", "clean"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, universal_newlines=True,)
##    proc = subprocess.Popen(["make"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, universal_newlines=True,)
##    print(proc.stdout.read())

#    import asyncio
#    async def run_make():
#        proc = await asyncio.create_subprocess_exec("make", "clean", stdout=asyncio.subprocess.PIPE)
##        data = await proc.stdout.readline()
##        print(data)
#        return proc
#
#    loop = asyncio.get_event_loop()
#    proc = loop.run_until_complete(run_make())
#    loop.close()

#    proc = await run_make()
#    await run_make()
#        import subprocess
#        proc = subprocess.Popen(["make", "clean"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, universal_newlines=True)
#        return proc

#    await proc = run_proc()
#    asyncio.run(run_proc())

#    print(type(proc))
#    print(proc.stdout.read())

#    proc = subprocess.Popen(["make"], bufsize=1, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#    proc = subprocess.Popen(["make"], bufsize=0, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#    outs, errs = proc.communicate(timeout=15)
#
#    print(outs)
#    print(errs)

#    try:
#        outs, errs = proc.communicate(timeout=15)
#    except TimeoutExpired:
#        proc.kill()
#        outs, errs = proc.communicate()

#    with click.progressbar(length=100, width=0, label="Configure PETSc", ) as bar:
#        for item in bar:
##            print(type(item))
##            print(item)
#            if item > 50:
#                break
#            time.sleep(0.05)

#    with click.progressbar(length=100, width=0, label="Configure PETSc", show_pos=True, item_show_func=my_func) as bar:
#            print(item)
#        for item in items:
#            time.sleep(0.05)
#            bar.update(item)

#    proc = subprocess.Popen(["make", "clean"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#    proc = subprocess.Popen(["make", "clean"])
#    proc = subprocess.Popen(["make", "clean"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#    proc = subprocess.Popen(["make"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#    proc = subprocess.Popen(["make"], stdout=subprocess.PIPE)

#metos3d_conf_file = "metos3d.conf.yaml"
#metos3d_conf_message = """
#### ERROR: No Metos3D configuration file found
#
#
#"""
#
#def info_show_configuration(ctx):
#    metos3d_conf = yaml.load(open(metos3d_conf_file))
#    click.echo(metos3d_conf)
#    pass
#
#def info_show_message(ctx):
#    click.echo(metos3d_conf_message)
#    pass
#
#def info_item(ctx, item):
#    return ctx.item

#source ../env/de.dkrz.mistral.intelmpi.env.sh
#source ../env/generic.mpich.gcc.env.sh
#source ../../../development/metos3d/metos3d/metos3d/env/generic.mpich.gcc.env.sh
#            print(out.strip())
#                ctx.item = pattern[1]
#                print()
#                i = i + 1
#                print(out)
#                time.sleep(1.0)
#                           item_show_func=lambda item: info_item(ctx, item),
#        import time
#        i = 0
