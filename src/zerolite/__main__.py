#!/usr/bin/env python3
from arguments import arguments
import model

def train():
    ZeroLiteModel = model.SimplifiedChessNetwork().to(model.device())
    print(ZeroLiteModel)

def play():
    pass

def main():
    if arguments['train']: train()
    else: play()

if __name__ == '__main__':
    main()