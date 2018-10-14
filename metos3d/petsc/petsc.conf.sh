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

# set compiler variables, CC, CXX,FC
#source ../env/de.dkrz.mistral.intelmpi.env.sh
#source ../env/generic.mpich.gcc.env.sh
source ../../../development/metos3d/metos3d/metos3d/env/generic.mpich.gcc.env.sh

#curl -O http://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc-3.10.2.tar.gz
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
--CC="$CC" \
--CXX="$CXX" \
--FC="$FC" \
--COPTFLAGS="-O3" \
--CXXOPTFLAGS="-O3" \
--FCOPTFLAGS="-O3" \
--download-yaml=1 \

#--download-fblaslapack=1 \
#--download-hdf5=1
#
#make

source deactivate metos3d-petsc-python2
conda remove --yes --name metos3d-petsc-python2 --all


