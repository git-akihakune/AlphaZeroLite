#!/usr/bin/env python3
import model
import chess


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
        pass


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