import sys
import numpy as np
import matplotlib.pyplot as plt

def read_PETSc_vec(file):
    f = open(file, "rb")
    np.fromfile(f, dtype=">i4", count=1)
    nvec, = np.fromfile(f, dtype=">i4", count=1)
    v = np.fromfile(f, dtype=">f8", count=nvec)
    f.close()
    return v

def read_PETSc_matrix(file):
    f = open(file,'rb')
    np.fromfile(f, dtype=">i4", count=1)     # PETSc matrix cookie
    nrow   = int(np.fromfile(f, dtype=">i4", count=1))      # number of rows
    ncol   = int(np.fromfile(f, dtype=">i4", count=1))      # number of columns
    nnzmat, = np.fromfile(f, dtype=">i4", count=1)      # number of nonzeros
    nnzrow = np.fromfile(f, dtype=">i4", count=nrow)   # number of nonzeros per row
    colind = np.fromfile(f, dtype=">i4", count=nnzmat) # column indices
    aij    = np.fromfile(f, dtype=">f8", count=nnzmat) # nonzeros
    f.close()
    A = np.zeros((nrow, ncol))
    start = 0
    for i in range(nrow):
         if nnzrow[i] != 0:
             end = start + nnzrow[i]
             A[i,colind[start:end]] = aij[start:end]
             start = end
    return A

def reshape_vector_to_3d(landSeaMask, v):
    # landseamask has shape latitude x longitude
    # we want the output to have longitude x latitude
    landSeaMask = np.transpose(landSeaMask)
    n1, n2 = np.shape(landSeaMask)
    n3 = int(np.amax(landSeaMask))
    v3d = np.nan * np.ones((n1,n2,n3))
    offset = 0
    # v is stored latitude x longitude
    for j in range(n2):
         for i in range(n1):
             if landSeaMask[i,j] != 0:
                 n = int(landSeaMask[i,j])
                 v3d[i,j,:n] = v[offset:offset + n]
                 offset = offset + n
    return v3d, n1, n2, n3

def blocksize(landSeaMask):
    # returns sizes of blocks in transport matrices
    # landseamask has shape latitude x longitude
    # we want the output to have longitude x latitude
    landSeaMask = np.transpose(landSeaMask)
    n1, n2 = np.shape(landSeaMask)
    n3 = int(np.amax(landSeaMask))
    bs = []
    # matrix indices are ordered latitude x longitude
    for j in range(n2):
         for i in range(n1):
             if landSeaMask[i,j] != 0:
                 bs.append(int(landSeaMask[i,j]))
    return bs
