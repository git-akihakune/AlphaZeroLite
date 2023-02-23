#!/usr/bin/env python3

"""
ZeroLite - Alpha Zero chess in a library.

Usage:
    zerolite train [--data <path>] [-out <path>] [--verbose]
    zerolite play [-d <path>] [--test] [--uci]
    zerolite -h | --help
    zerolite --version

Options:
    -d --data PATH  Path to dataset/model.
    -o --out PATH   Model save location.
    -h --help       Show this screen.
    -t --test       Run in debug mode.
    -u --uci        Run with UCI.
    -v --verbose    Run in verbose mode.
    -V --version    Show version.
"""
from docopt import docopt
import globalval

arguments = docopt(__doc__, version=f"ZeroLite {globalval.version}")