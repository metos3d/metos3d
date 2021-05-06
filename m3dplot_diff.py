#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt
import petsc_mod as pe


def m3dplot_diff(file1, file2, layer):
    # file 'landSeaMask.petsc' has to be in the current directory
    lsm = pe.read_PETSc_matrix('landSeaMask.petsc')
    v1 = pe.read_PETSc_vec(file1)
    v2 = pe.read_PETSc_vec(file2)
    v = v1-v2
    v3d, n1, n2, n3 = pe.reshape_vector_to_3d(lsm, np.abs(v))
    # print(v3d)
    long, lat = np.meshgrid(np.linspace(-90,90,n2),np.linspace(0,360,n1))
    plt.contourf(lat,long,v3d[:,:,layer])
    plt.colorbar()
    plt.title('data: |' + file1 + ' - ' + file2 + '|,  layer = ' + str(layer))
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.show()

#
#   main
#
if __name__ == "__main__":
    # usage: m3dplot_diff.py filename1 filename2 layer
    # file 'landSeaMask.petsc' has to be in the current directory
    if len(sys.argv) < 4:
        print("\nNot enough input arguments!")
        print("Usage: m3dplot_diff.py filename1 filename2 layer")
        print("Plots absolute difference of data in filename1, filename2 in a vertical layer.")
        print("File 'landSeaMask.petsc' has to be in the current directory.\n")
        exit()
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    layer = int(sys.argv[3])
    m3dplot_diff(file1, file2, layer)
