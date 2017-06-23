#
# Metos3D: A Marine Ecosystem Toolkit for Optimization and Simulation in 3-D
# Copyright (C) 2012  Jaroslaw Piwonski, CAU, jpi@informatik.uni-kiel.de
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

# object files
M3DOBJSC = \
	simpack/src/metos3d_debug.o \
	simpack/src/metos3d_util.o \
	simpack/src/metos3d_geometry.o \
	simpack/src/metos3d_load.o \
	simpack/src/metos3d_bgc.o \
	simpack/src/metos3d_transport.o \
	simpack/src/metos3d_timestep.o \
	simpack/src/metos3d_solver.o \
	simpack/src/metos3d_init.o \
	simpack/src/metos3d.o

# BGC model name
BGCMODELNAME = $(notdir $(BGC:%/=%))
BGCMODELOBJ = model.o
# if a model Makefile.in exists, use it
# Makefile.in must declare object files in the BGCMODELOBJ variable
-include $(BGC)/Makefile.in
M3DOBJSBGC = $(addprefix $(BGC)/, $(BGCMODELOBJ))

# executable name
PROGRAMBASE = metos3d-simpack-
PROGRAM = ${PROGRAMBASE}${BGCMODELNAME}.exe

ALL: $(PROGRAM)
CFLAGS = -DBGC=metos3dbgc_ -DBGCINIT=metos3dbgcinit_ -DBGCFINAL=metos3dbgcfinal_
FFLAGS = 
CLEANFILES = $(M3DOBJSBGC) $(M3DOBJSC) $(PROGRAM)

include $(PETSC_DIR)/lib/petsc/conf/variables
include $(PETSC_DIR)/lib/petsc/conf/rules

$(PROGRAM): $(M3DOBJSBGC) $(M3DOBJSC) chkopts
	-$(CLINKER) -o $@ $(M3DOBJSBGC) $(M3DOBJSC) $(PETSC_LIB)
