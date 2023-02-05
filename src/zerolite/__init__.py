#!/usr/bin/env python3

from importlib import resources
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

# Package constants
__name__ = 'zerolite'
__version__ = '0.0.1'
__description__ = "Chess neural network based on Alpha Zero's algorithm"
__url__ = 'https://github.com/git-akihakune/AlphaZeroLite'
__author__ = 'Aki Hakune'
__license__ = 'MIT'