#!/usr/bin/env python

#
#   main
#
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print '''Example usage:
  ./metos3d [info | home | options ] [FORMULA...]
  brew install FORMULA...
  brew uninstall FORMULA...
  brew search [foo]
  brew list [FORMULA...]
  brew update
  brew upgrade [FORMULA...]

Troubleshooting:
  brew doctor
  brew install -vd FORMULA
  brew [--env | --config]

Brewing:
  brew create [URL [--no-fetch]]
  brew edit [FORMULA...]
  open https://github.com/mxcl/homebrew/wiki/Formula-Cookbook

Further help:
   man brew
  brew home'''
    else:
        sys.exit(0)
