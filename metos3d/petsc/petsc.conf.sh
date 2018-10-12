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

# set compiler variables,
# METOS3D_CC
# METOS3D_CXX
# METOS3D_FC
# source generic.mpich.gcc.env.sh

#tar -xzf petsc-lite-3.10.2.tar.gz
#cd petsc-3.10.2/

conda create --yes --name metos3d-petsc-python2 python=2
source activate metos3d-petsc-python2

export PETSC_DIR=`pwd`
export PETSC_ARCH=arch-metos3d-petsc

./configure \
--scrollOutput=1 \
--with-debugging=0 \
--with-x=0 \
--CC="$METOS3D_CC" \
--CXX="$METOS3D_CXX" \
--FC="$METOS3D_FC" \
--COPTFLAGS="-O3" \
--CXXOPTFLAGS="-O3" \
--FCOPTFLAGS="-O3" \
--download-yaml=1 \

#> configure_lines.txt
#--download-fblaslapack=1 \
#--download-hdf5=1

# wc configure_lines.txt
# 430    1704   60983 configure_lines.txt

# make >
# make_lines.txt

# wc make_lines.txt
# 1583    3810  102160 make_lines.txt

source deactivate metos3d-petsc-python2
conda remove --yes --name metos3d-petsc-python2 --all


