#!/usr/bin/env python3
from setuptools import setup
import zerolite

setup(
    name=zerolite.__name__,
    version=zerolite.__version__,
    description=zerolite.__description__,
    url=zerolite.__url__,
    author=zerolite.__author__,
    license=zerolite.__license__,
    packages=['zerolite'],
    install_requires=[
        'torch>=1.13.1',
        'python-chess',
        'docopt'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Education :: Testing',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ]
)