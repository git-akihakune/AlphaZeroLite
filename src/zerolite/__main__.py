#!/usr/bin/env python3
from arguments import arguments
import model
import interface

def train():
    ZeroLiteModel = model.ZeroLiteNetwork().to(model.device())
    print(ZeroLiteModel)

def play():
    game = interface.UCI() if arguments['--uci'] else interface.TUI()
    game.play()

def main():
    if arguments['train']: train()
    else: play()

if __name__ == '__main__':
    main()