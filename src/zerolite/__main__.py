#!/usr/bin/env python3
from arguments import arguments
import model
import simulation

def train():
    ZeroLiteModel = model.ZeroLiteNetwork().to(model.device())
    print(ZeroLiteModel)

def play():
    if arguments['--test']: firstPlayer, secondPlayer = [simulation.Human()] * 2
    elif arguments['--black']: firstPlayer, secondPlayer = [model.Randomizer(), simulation.Human()]
    else: firstPlayer, secondPlayer = [simulation.Human(), model.Randomizer()]
    game = simulation.Simulator()
    game.play(firstPlayer, secondPlayer)

def main():
    if arguments['train']: train()
    else: play()

if __name__ == '__main__':
    main()