#!/usr/bin/env python3
from arguments import arguments
import model
import interface

def train():
    ZeroLiteModel = model.ZeroLiteNetwork().to(model.device())
    print(ZeroLiteModel)

def play():
    opponent = model.Randomizer()
    simulation = interface.Simulation()
    simulation.play('white', opponent)

def main():
    if arguments['train']: train()
    else: play()

if __name__ == '__main__':
    main()