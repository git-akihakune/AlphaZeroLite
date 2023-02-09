#!/usr/bin/env python3
from zerolite import model

def main():
    ZeroLiteModel = model.SimplifiedChessNetwork().to(model.device())
    print(ZeroLiteModel)

if __name__ == '__main__':
    main()