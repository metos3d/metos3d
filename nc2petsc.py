#!/usr/bin/env python

import sys
import numpy as np
import netCDF4 as nc4

#
#   extract_data_vector_sequence
#
#   order of extraction 3D:
#   at the (y, x) point, the whole water column (z)
#
def extract_data_vector_sequence(netcdf_file, variable_name, grid_file):
    print("extracting ...", netcdf_file, variable_name, grid_file)

    # open grid file
    rootgrp = nc4.Dataset(grid_file, "r")
    # netcdf variable
    grid_mask_variable = rootgrp.variables["grid_mask"]
    # numpy masked array
    grid_mask = grid_mask_variable[0,0,:,:]
    # get sizes, we expect  (y, x)
    ny, nx = grid_mask.shape
    print("grid mask dimensions:", "ny:", ny, "nx:", nx)

    # open netcdf file
    rootgrp = nc4.Dataset(netcdf_file, "r")
    # get variable
    var = rootgrp.variables[variable_name]
    # get sizes, we expect  (time, y, x)
    nt, ny, nx = var.shape
    print("variable dimensions:", "nt:", nt, "ny:", ny, "nx:", nx)

    # loop over time
    y = []
    for it in range(nt):
        # get array
        var_array = var[it,:,:]
        # get values
        var_values = var_array[~grid_mask.mask]
        # append to list
        y.append(var_values)

    return y

#
#   save_sequence_as_petsc_vectors
#
def save_sequence_as_petsc_vectors(output_file_name, y):
    print("save as petsc vectors ...")
    # loop over data vectors
    for ivec in range(len(y)):
        # construct filename
        filename = "%s%02d.petsc" % (output_file_name, ivec)
        print(filename)
        
        # open file
        f = open(filename, 'wb+')
        # header
        # petsc vecid 1211214
        np.asarray(1211214, dtype = '>i4').tofile(f)
        # vector length
        nvec = y[ivec].size
        np.asarray(nvec,    dtype = '>i4').tofile(f)
        # vector values
        np.asarray(y[ivec], dtype = '>f8').tofile(f)
        f.close()

#
#   main
#
if __name__ == "__main__":
    # no arguments?
    if len(sys.argv) <= 4:
        # print usage and exit with code 1
        print("usage: %s [netcdf-file] [variable-name] [grid-file] [output-file-prefix]" % sys.argv[0])
        sys.exit(1)
    # netcdf file
    netcdf_file = sys.argv[1]
    # variable name
    variable_name = sys.argv[2]
    # grid file
    grid_file = sys.argv[3]
    # output file prefix
    output_file_prefix = sys.argv[4]
    # extract data vector sequence
    y = extract_data_vector_sequence(netcdf_file, variable_name, grid_file)
    # save sequence as petsc vectors
    save_sequence_as_petsc_vectors(output_file_prefix, y)


