"""
This Helper file contain methods and vars to help
the players to focus only on the best move to make
on the BoardGame
"""
from Properties import *

def GetOpponent(Char):
    if Char is X: return O
    return X

def GetAvailableMoves(GameBoard):
    return [Item for Item, Value in enumerate(GameBoard) if Value is Empty]