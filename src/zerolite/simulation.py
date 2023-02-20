#!/usr/bin/env python3
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

class Simulator():
    def __init__(self) -> None:
        self.board = chess.Board()
        
    def play(self, firstPlayer, secondPlayer):
        numberOfMove = 0
        while not self.board.is_game_over():
            print(self.board)
            if numberOfMove % 2 == 0: self.board.push_san(firstPlayer.move(self.board))
            else: self.board.push_san(secondPlayer.move(self.board))
            numberOfMove += 1
            print() # Separate previous and current move
        if self.board.outcome().termination.CHECKMATE:
            print(f"Game ended. {'White' if self.board.outcome().winner else 'Black'} won.")
        else:
            print(f"Game ended.")