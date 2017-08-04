#!/usr/bin/env python

import os
import sys
import re
import numpy as np
import netCDF4 as nc4
import yaml

#
#   read_PETSc_vec
#
def read_PETSc_vec(file):
    # debug
#    print("read_PETSc_vec ... %s" % file)
    # open file
    # omit header
    # read length
    # read values
    # close file
    f = open(file, "rb")
    np.fromfile(f, dtype=">i4", count=1)
    nvec, = np.fromfile(f, dtype=">i4", count=1)
    v = np.fromfile(f, dtype=">f8", count=nvec)
    f.close()
    return v

#
#   read_conf_file
#
def read_conf_file(conf_file):
    print("Reading configuration file ... " + conf_file)
    # open conf file
    f = open(conf_file, "r")
    # parse yaml file
    conf = yaml.load(f)
    # get list of variables
    conf_list = []
    try:
        var_list = conf["Name, Scale, Unit, Description"]
        # loop over list
        for var in var_list:
            # split
            name, scale, unit, description = var.split(",", 3)
            # strip and convert
            name = name.strip()
            scale = float(scale.strip())
            unit = unit.strip()
            description = description.strip()
            # append to conf list
            conf_list.append({"name": name, "scale": scale, "unit": unit, "description": description})
    except KeyError:
        print("### ERROR ### Did not find the 'Name, Scale, Unit, Description' key.")
        sys.exit(1)
    # return results
    return conf_list

#
#   write_netcdf_file
#
def write_netcdf_file(grid_file, conf_list, petsc_data, out_netcdf_file):
    print("Writing NetCDF file ... " + out_netcdf_file)

    # open grid file
    grid_nc4 = nc4.Dataset(grid_file, "r")
    # netcdf variable
    try:
        grid_mask_variable = grid_nc4.variables["grid_mask"]
    except KeyError:
        print("### ERROR ### No 'grid_mask' variable found.")
        sys.exit(1)
    # numpy masked array
    grid_mask = grid_mask_variable[0,:,:,:]
    # get sizes, we expect  (y, x)
    nz, ny, nx = grid_mask.shape
    print("Grid mask dimensions ... ", "nz:", nz, "ny:", ny, "nx:", nx)

    # create netcdf file
    out_file = nc4.Dataset(out_netcdf_file, "w", format = "NETCDF4")
    # set usage of fill value
    out_file.set_fill_on()
    # create global attributes
    out_file.description = "Metos3D tracer file for 2.8125 degree, 15 layers MITgcm resolution"
    out_file.history = "created with: %s %s %s %s" % (sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3])

    # copy dimensions from grid file
    for dimname, dim in grid_nc4.dimensions.items():
        out_file.createDimension(dimname, len(dim))
        out_file.sync()

    # copy variables
    for varname, ncvar in grid_nc4.variables.items():
        if varname in ["time", "depth", "lat", "lon"]:
            var = out_file.createVariable(varname, ncvar.dtype, ncvar.dimensions, zlib = True, fill_value = -9.e+33)
            attdict = ncvar.__dict__
            var.setncatts(attdict)
            var[:] = ncvar[:]
            out_file.sync()

    # create variables
    work_array = grid_mask.reshape(nz, ny*nx).transpose().flatten()
    for var_list in conf_list:
        print(var_list)
        var = out_file.createVariable(var_list["name"], "f8", ("time", "depth", "lat", "lon", ), zlib = True, fill_value = -9.e+33)
        var.unit = var_list["unit"]
        var.description = var_list["description"]
        # transform from 1d to 3d
        work_array[~work_array.mask] = petsc_data[var_list["name"]]
        var[0,:,:,:] = work_array.reshape(ny*nx, nz).transpose().reshape(nz, ny, nx)
    
    # close file
    out_file.close()

#
#   get_data_from_petsc_file
#
def get_data_from_petsc_file(conf_list):
    print("Opening PETSc files ...")
    # loop over names
    petsc_data = {}
    for conf in conf_list:
        # read petsc file
        petsc_file = "work/" + conf["name"] + ".petsc"
        petsc_vec = read_PETSc_vec(petsc_file)
        # store
        petsc_data[conf["name"]] = petsc_vec
    return petsc_data

#
#   main
#
if __name__ == "__main__":
    # no arguments?
    if len(sys.argv) <= 3:
        # print usage and exit with code 1
        print("usage: %s [grid-netcdf-file] [conf-yaml-file] [out-netcdf-file]" % sys.argv[0])
        sys.exit(1)
    # grid file
    grid_file = sys.argv[1]
    # conf yaml file
    conf_yaml_file = sys.argv[2]
    # out netcdf file
    out_netcdf_file = sys.argv[3]
    # debug
#    print(conf_yaml_file, out_netcdf_file)
    # read conf file
    conf_list = read_conf_file(conf_yaml_file)
    # debug
#    print(conf_list)
    # get data from petsc file
    petsc_data = get_data_from_petsc_file(conf_list)
    # debug
#    print(petsc_data)
    # write netcdf file
    write_netcdf_file(grid_file, conf_list, petsc_data, out_netcdf_file)


