# AlphaZeroLite
A neural network model based on DeepMind Alpha Zero's paper.

## Developer's note
This repository was only made for learning and demonstrating purposes. Therefore, **all changes are pushed directly to the main branch for development transparency**. Aside from that, common development practices are applied.

## Installation
### For end-user
This module will be developed to be compatible as a `pip` module. In this current phase, 
### For developer
For bleeding-edge installation, first clone this repo:
```bash
git clone https://github.com/git-akihakune/AlphaZeroLite.git
```

Then get into the `src` directory:
```bash
cd src
```

And run the development instance from there:
```
$ python zerolite -h
ZeroLite - Alpha Zero chess in a library.

Usage:
    zerolite train [--data <path>] [-out <path>]
    zerolite play [--model <path>] [--test][--black]
    zerolite -h | --help
    zerolite --version

Options:
    -b --black      Play as black
    -d --data PATH  Path to dataset.
    -o --out PATH   Model save location.
    -m --model PATH Path to saved model.
    -h --help       Show this screen.
    -t --test       Run in debug mode.
    -v --version    Show version.
```


