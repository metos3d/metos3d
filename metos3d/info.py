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

"""Methos3D Info python file"""

import click
import metos3d

@click.command("info")
@click.pass_context
def info_cli(ctx):
    """Show Metos3D configuration"""
    metos3d_conf = metos3d.read_config(ctx)
    metos3d.echo("Metos3D environment", metos3d_conf["metos3d"]["env"])
    metos3d.echo("PETSc library", metos3d_conf["metos3d"]["petsc"])
    metos3d.echo("Metos3D data", metos3d_conf["metos3d"]["data"])
    metos3d.echo("Metos3D model", metos3d_conf["metos3d"]["model"])


