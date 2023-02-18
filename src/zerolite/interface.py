#!/usr/bin/env python3
import chess

class Simulation():
    def __init__(self) -> None:
        self.board = chess.Board()
        
    def play(self, playerPosition:str, opponent):
        isYourTurn = True if playerPosition == 'white' else False
        while not (
            self.board.is_checkmate() or
            self.board.is_stalemate() or
            self.board.can_claim_draw() or 
            self.board.can_claim_fifty_moves() or
            self.board.is_insufficient_material()
        ):
            print(self.board)
            if isYourTurn:
                try:
                    self.board.push_san(input("Enter a valid move: "))
                    isYourTurn = False
                except:
                    print("Unvalid move detected. Game terminating...")
                    exit()
            else:
                self.board.push_san(opponent.predict(self.board))
                isYourTurn = True