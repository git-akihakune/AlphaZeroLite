#!/usr/bin/env python3
import model
import chess
from zerolite import globalval


class Human():
    def move(self, board):
        while True:
            move = input("Enter a valid move: ")
            if move not in [str(move) for move in board.legal_moves]:
                print(f"Invalid move detected. The valid moves are: {[str(move) for move in board.legal_moves]}. Please try again.")
                continue
            break
        return move


def UCI():
    def __init__(self):
        try:
            from threading import Thread
            self.debug = False
            self.setup = False
            self.name = f"{globalvar.name} {globalvar.version}"
        except:
            print("registration error")

    def receiveCommand(self):
        while True:
            self._handleCommand(input())

    def _handleCommand(self, command:str) -> str:
        """Process commands according to UCI standard"""
        options = command.split()[1:]
        command = command.split()[0]

        if command == "uci":
            self._id()
        elif command == "debug":
            self.debug = True if options[0] == "on" else False
        elif command == "isready":
            self._isReady()
        elif command == "setoption":
            self._setOption(options)
        elif command == "register":
            self._register(options)
            
    def internalSetup(self):
        self.board = chess.Board()
        self.setup = True

    def calculate():
        pass

    def _id(self):
        print(f"id name {self.name}")
        print(f"id author {globalvar.author}")

    def _isReady(self):
        if not self.setup: self.internalSetup()
        print("readyok")

    def _setOption(self, options):
        name = options[1]
        value = options[3]
        setattr(self, name, value)

    def _register(self, options):
        if options[0] == "name":
            self.name = options[1:].join(' ')
        elif options[0] == "code":
            self.code = options[1]
        else: pass

    def play(self):
        Thread(target=receiveCommand(self)).start()


class TUI():
    def __init__(self) -> None:
        self.board = chess.Board()
        self._printBanner()
        self.white, self.black = self._assignPosition()

    @staticmethod
    def _printBanner():
        print("ZeroLite - Your own model of Alpha Zero chess.")
        print("Aki Hakune © 2023\n")

    def _assignPosition(self) -> list():
        choice = input("Play as black or white? [b/w] ")
        if choice == 'b':
            return [model.Randomizer(), Human()]
        elif choice == 'w':
            return [Human(), model.Randomizer()]

        print("No legit choice submitted. Exiting...") #TODO: Move this to error level after implementing verbose mode
        exit()
        return [] # To silent from warnings
        
    def play(self):
        numberOfMove = 0
        while not self.board.is_game_over():
            print(self.board)
            if numberOfMove % 2 == 0: self.board.push_san(self.white.move(self.board))
            else: self.board.push_san(self.black.move(self.board))
            numberOfMove += 1
            print() # Separate previous and current move
        if self.board.outcome().termination.CHECKMATE:
            print(f"Game ended. {'White' if self.board.outcome().winner else 'Black'} won.")
        else:
            print(f"Game ended.")