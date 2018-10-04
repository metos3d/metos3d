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

from . import version
from . import info
from . import config
from . import simpack
from . import optpack
from . import data
from . import model

__all__ = (
           "__title__",
           "__summary__",
           "__uri__",
           "__version__",
           "__author__",
           "__email__",
           "__license__",
           "__copyright__",
           )

__title__       = "metos3d"
__summary__     = "Marine Ecosystem Toolkit for Optimization and Simulation in 3-D"
__uri__         = "https://github.com/metos3d"

__version__     = version.__version__

__author__      = "Jaroslaw Piwonski (CAU)"
__email__       = "jpi@informatik.uni-kiel.de"

__license__     = "GPL-3.0"
__copyright__   = "Copyright 2018 Jaroslaw Piwonski"


