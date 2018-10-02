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

from setuptools import setup
import metos3dpy

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(name                          = metos3dpy.__title__,
      version                       = metos3dpy.__version__,
      description                   = metos3dpy.__summary__,
      long_description              = long_description,
      long_description_content_type = "text/markdown",
      url                           = metos3dpy.__uri__,
      author                        = metos3dpy.__author__,
      author_email                  = metos3dpy.__email__,
      license                       = metos3dpy.__license__,
      packages                      = ["metos3dpy"],
      entry_points                  = {
        "console_scripts": ["metos3d=metos3dpy.metos3d:metos3d"],
      },
      install_requires              = ["click", "pyyaml"],
      zip_safe                      = False)
