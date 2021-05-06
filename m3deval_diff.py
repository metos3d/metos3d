#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt
import petsc_mod as pe


def m3deval_diff(file1, file2):
    # file 'landSeaMask.petsc' has to be in the current directory
    lsm = pe.read_PETSc_matrix('landSeaMask.petsc')
    v1 = pe.read_PETSc_vec(file1)
    v2 = pe.read_PETSc_vec(file2)
    v3d1, n1, n2, n3 = pe.reshape_vector_to_3d(lsm, v1)
    v3d2, n1, n2, n3 = pe.reshape_vector_to_3d(lsm, v2)
    v3d1 = np.nan_to_num(v3d1)
    v3d2 = np.nan_to_num(v3d2)
    # compute differences per layer in different norms:
    print("layer          abs diff    rel diff ||.||_2")
    for i in range(n3):
        i_str = "%5i" % i
        absdiff = np.linalg.norm(v3d1[:,:,i]-v3d2[:,:,i],'fro')
        abs_str = "%10.4f"  % absdiff
        reldiff = absdiff/np.linalg.norm(v3d1[:,:,i],'fro')
        rel_str = "%10.4f"  % reldiff
        print(i_str + "       " + abs_str + " " + rel_str)
    absdiff = np.linalg.norm(v1-v2)
    abs_str = "%10.4f"  % absdiff
    reldiff = absdiff/np.linalg.norm(v1)
    rel_str = "%10.4f"  % reldiff
    print("  all       " + abs_str + " " + rel_str)

#
#   main
#
if __name__ == "__main__":
    print("\nUsage: m3eval_diff.py filename1 filename2\n")
    print("Evaluates absolute and relative difference of data")
    print("in filename1, filename2 in Euclidean norm for all layers")
    print("(relative diff wrt data in first input file).\n")
    print("File 'landSeaMask.petsc' has to be in the current directory.\n")
    if len(sys.argv) < 3:
        print("Not enough input arguments!")
        exit()
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    m3deval_diff(file1, file2)
