#!/usr/bin/env python

import os
import sys
import re
import yaml

import matplotlib
matplotlib.rc("font", **{"family" : "sans-serif"})
matplotlib.rcParams.update({'font.size': 14})
#matplotlib.rc("text", usetex = True)
matplotlib.use("PDF")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages as pdfpages


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
#   read_output_file
#
def read_output_file(conf_list, text_in_file):
    print("Reading output file ... " + text_in_file)
    # init
    figure_data = {}
    var_name = []
    for conf in conf_list:
        name = conf["name"]
        figure_data[name] = []
        var_name.append(name)
    # read file, parse and store
    f = open(text_in_file, "r")
    for line in f:
#        print(line)
        # match variable
        for name in var_name:
#            print(name)
            var_match = re.search("^.+ \d+ .+: \d+, %s\s+, total:\s+([+-]\d+.\d+e[+-]\d+)" % name, line)
#            print(var_match)
            if var_match:
                figure_data[name].append(float(var_match.groups()[0]))
    # close file
    f.close()
    return figure_data

#
#   create_figures
#
def create_figures(conf_list, figure_data, pdf_out_file):
    print("Creating figures ... " + pdf_out_file)
    # create one pdf document with all figures
    pdf_pages = pdfpages(pdf_out_file)
    # loop over variables
    for conf in conf_list:
        # debug
        print(conf)
        # name, unit, data
        name = conf["name"]
        data = figure_data[name]
        unit = conf["unit"]
        # plot
        fig = plt.figure()
        plt.plot(data, 'k')
        plt.title("%s" % name)
        plt.xlabel("model years")
        plt.ylabel("[%s]" % unit)
        # store
        pdf_pages.savefig(fig)
        # close figure
        plt.close()
    # close pdf doc
    pdf_pages.close()

#
#   main
#
if __name__ == "__main__":
    # no arguments?
    if len(sys.argv) <= 3:
        # print usage and exit with code 1
        print("usage: %s [conf-file] [text-in-file] [pdf-out-file]" % sys.argv[0])
        sys.exit(1)
    # conf file
    conf_file = sys.argv[1]
    # text in file
    text_in_file = sys.argv[2]
    # pdf out file
    pdf_out_file = sys.argv[3]
    # debug
    print(conf_file)
    print(text_in_file)
    print(pdf_out_file)
    # read conf file
    conf_list = read_conf_file(conf_file)
    # debug
#    print(conf_list)
    # read output file
    figure_data = read_output_file(conf_list, text_in_file)
    # debug
#    print(figure_data)
    # create figures
    create_figures(conf_list, figure_data, pdf_out_file)


