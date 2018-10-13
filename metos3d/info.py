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

import os
import yaml
import click

metos3d_conf_file = "metos3d.conf.yaml"
metos3d_conf_message = """
### ERROR: No Metos3D configuration file found


"""

def info_show_configuration(ctx):
    metos3d_conf = yaml.load(open(metos3d_conf_file))
    click.echo(metos3d_conf)
    pass

def info_show_message(ctx):
    click.echo(metos3d_conf_message)
    pass

def info(ctx):
    """
        Retrieve information from the configuration file.
    """

    import subprocess
    proc = subprocess.Popen(["source ../../../development/metos3d/metos3d/metos3d/petsc/petsc.conf.sh"], stdout=subprocess.PIPE, shell=True, stderr=subprocess.STDOUT)

    with click.progressbar(length=450, width=0, label="Configure PETSc", ) as bar:
        for item in bar:
            out = proc.stdout.readline()




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
