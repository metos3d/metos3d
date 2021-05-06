#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt
import petsc_mod as pe

def m3dplot(file, layer):
    # file 'landSeaMask.petsc' has to be in the current directory
    lsm = pe.read_PETSc_matrix('landSeaMask.petsc')
    v   = pe.read_PETSc_vec(file)
    v3d, n1, n2, n3 = pe.reshape_vector_to_3d(lsm, v)
    long, lat = np.meshgrid(np.linspace(-90,90,n2),np.linspace(0,360,n1))
    plt.contourf(lat,long,v3d[:,:,layer])
    plt.colorbar()
    plt.title('data: ' + file + ',  layer = ' + str(layer))
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.show()

#
#   main
#
if __name__ == "__main__":
    # usage: m3dplot.py filename layer
    # file 'landSeaMask.petsc' has to be in the current directory
    if len(sys.argv) < 3:
        print("\nNot enough input arguments!")
        print("Usage: m3dplot.py filename layer")
        print("Plots data in filename in a vertical layer.")
        print("File 'landSeaMask.petsc' has to be in the current directory.\n")
        exit()
    file = sys.argv[1]
    layer = int(sys.argv[2])
    m3dplot(file, layer)
