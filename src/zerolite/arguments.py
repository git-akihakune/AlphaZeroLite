#!/usr/bin/env python3

"""
ZeroLite - Alpha Zero chess in a library.

Usage:
    zerolite train [--data <path>] [-out <path>]
    zerolite play [--model <path>]
    zerolite -h | --help
    zerolite --version

Options:
    -d --data PATH  Path to dataset.
    -o --out PATH   Model save location.
    -m --model PATH Path to saved model.
    -h --help       Show this screen.
    -v --version    Show version.
"""
from docopt import docopt
import globalval

arguments = docopt(__doc__, version=f"ZeroLite {globalval.version}")