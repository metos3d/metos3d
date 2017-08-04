#!/usr/bin/env python

import os
import sys
import re

import matplotlib
matplotlib.rc("font", **{"family" : "sans-serif"})
matplotlib.rcParams.update({'font.size': 14})
#matplotlib.rc("text", usetex = True)
matplotlib.use("PDF")
import matplotlib.pyplot as plt

#
#   create_hamocc_figures
#
def create_hamocc_figures(filepath, tracer_name_unit, tracer_data, diag_name_unit, diag_data):
    print("Creating tracer and diagnostic figures ... " + filepath)
    # loop over tracers
    for (name, unit) in tracer_name_unit:
        # plot
#        print(name)
#        print(unit)
#        print(tracer_data[name])
        plt.figure()
        plt.plot(tracer_data[name], 'k')
        plt.title("%s" % name)
        plt.xlabel("model years")
        plt.ylabel("[%s]" % unit)
#        ax = p.axes
#        ax.title()
        # write to file
        plt.savefig("%s%s.pdf" % (filepath, name), bbox_inches = "tight")
        plt.close()
    # loop over diag
    for (name, unit) in diag_name_unit:
        # plot
#        print(name)
#        print(unit)
#        print(diag_data[name])
        plt.figure()
        plt.plot(diag_data[name], 'k')
        plt.title("%s" % name)
        plt.xlabel("model years")
        plt.ylabel("[%s]" % unit)
#        ax = p.axes
#        ax.title()
        # write to file
        plt.savefig("%s%s.pdf" % (filepath, name), bbox_inches = "tight")
        plt.close()


#
#   read_hamocc_tracer_and_diag_data
#
def read_hamocc_tracer_and_diag_data(outfile, tracer, diag):
    print("Reading tracer and diagnostic data ... " + outfile)
    # init
    tracer_data = {}
    for name in tracer:
        tracer_data[name] = []
    diag_data = {}
    for name in diag:
        diag_data[name] = []
    # read file, parse and store
    f = open(outfile, "r")
    for line in f:
#        print(line)
        # match tracer
        for name in tracer:
#            print(name)
            tracer_match = re.search("^.+ \d+ Tracer: \d+, %s\s+, total:\s+([+-]\d+.\d+e[+-]\d+)" % name, line)
#            print(tracer_match)
            if tracer_match:
                tracer_data[name].append(float(tracer_match.groups()[0]))
        # match diagnostic variable
        for name in diag:
#            print(name)
            diag_match = re.search("^.+ \d+ Diagnostics: \d+, %s\s+, total:\s+([+-]\d+.\d+e[+-]\d+)" % name, line)
#            print(diag_match)
            if diag_match:
                diag_data[name].append(float(diag_match.groups()[0]))
    # close file
    f.close()
    # return results
    return tracer_data, diag_data

#
#   read_conf_file
#
def read_conf_file(conf_file):
    print("Reading configuration file ... " + conf_file)
    # read file, parse and store
    f = open(conf_file, "r")
    # output file
    # tracer names
    # tracer units
    outfile     = f.readline().strip()
    tracer      = f.readline().strip().split(",")
    tracer_unit = f.readline().strip().split(",")
    diag        = f.readline().strip().split(",")
    diag_unit   = f.readline().strip().split(",")
    # return results
    return outfile, tracer, tracer_unit, diag, diag_unit

#
#   main
#
if __name__ == "__main__":
    # no arguments?
    if len(sys.argv) <= 1:
        # print usage and exit with code 1
        print("usage: %s [conf-file...]" % sys.argv[0])
        sys.exit(1)
    
    # read configuration file
    conf_file = sys.argv[1]
    outfile, tracer, tracer_unit, diag, diag_unit = read_conf_file(conf_file)
#    print(outfile, tracer, tracer_unit, diag, diag_unit)

    # read and parse output file
    filepath = os.path.dirname(conf_file) + "/" + outfile
    tracer_data, diag_data = read_hamocc_tracer_and_diag_data(filepath, tracer, diag)
#    print(tracer_data, diag_data)

    # create figures
    filepath = os.path.dirname(conf_file) + "/work/"
    tracer_name_unit = zip(tracer, tracer_unit)
    diag_name_unit = zip(diag, diag_unit)
    create_hamocc_figures(filepath, tracer_name_unit, tracer_data, diag_name_unit, diag_data)


