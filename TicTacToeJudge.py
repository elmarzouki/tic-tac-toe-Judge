"""
about:
This code was written by Mostafa El-Marzouki @iSuperMostafa
------------------------------------------------------------
summery:
this judge allows you to focus on choosing the best position to play
tic-tac-toe game Just by write your code in BotNumOne or BotNumTwo
--------------------------------------------------------------------------------------------
                                        Tic-Tac-Toe Judge
--------------------------------------------------------------------------------------------
The goal of Tic-Tac-Toe is to be the first player to get three in a row on a 3x3 grid.
X always goes first.
Players alternate placing Xs and Os on the board until either
(a) One player has three in a row, horizontally, Vertically or diagonally.
(b) All nine squares are filled.
"""
import random
from Helper import *

class TicTacToeJudge:
    # ini the game attributes
    def __init__(self, BotNumOneObj, BotNumTwoObj):
        self.GameBoard = [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty]
        self.BotNumOne = {'Name': Empty, 'Turn': Empty, 'Play': BotNumOneObj}
        self.BotNumTwo = {'Name': Empty, 'Turn': Empty, 'Play': BotNumTwoObj}
        """
        # In Tic-Tac-Toe there's 8 possible winning positions
        # across the top, across the middle, across the bottom,
        #  down the left side, down the middle, down the right side,
        # 45 diagonal and 135 diagonal
        """
        self.BotTurn = X
        self.IsGameEnded = False
        self.Winner = Empty
        self.IsGameStarted = False

    # Randomly choose which bot to start the game
    def GoFirst(self):
        if random.choice((X, O)) == X:
            self.BotNumOne['Turn'] = X
            self.BotNumTwo['Turn'] = O
        else:
            self.BotNumTwo['Turn'] = X
            self.BotNumOne['Turn'] = O
        self.IsGameStarted = True

    # place the player's move on the board
    def MakeMove(self, char, position):
        if self.GameBoard[position] is Empty:
            self.GameBoard[position] = char
        else:
            self.TakeTurns()

    # place the player's moves while the game not ended
    def TakeTurns(self):
        # if all(item is Empty for item in self.GameBoard):
        if not self.IsGameStarted:
            self.GoFirst()
        while not self.IsGameEnded:
            if self.BotNumOne['Turn'] is self.BotTurn:
                position = self.BotNumOne['Play'].play(self.GameBoard, self.BotNumOne['Turn'])
                self.MakeMove(self.BotNumOne['Turn'], position)
                self.BotTurn = self.BotNumTwo['Turn']
                self.IsWinner()
            elif self.BotNumTwo['Turn'] is self.BotTurn:
                position = self.BotNumTwo['Play'].play(self.GameBoard, self.BotNumTwo['Turn'])
                self.MakeMove(self.BotNumTwo['Turn'], position)
                self.BotTurn = self.BotNumOne['Turn']
                self.IsWinner()
        return self.Winner, self.GameBoard

    def IsWinner(self):
        for Char in (self.BotNumOne['Turn'], self.BotNumTwo['Turn']):
            Moves = [Move for Move, Value in enumerate(self.GameBoard) if Value == Char]
            for WinningState in WinningStates:
                winner = True
                for Move in WinningState:
                    if Move not in Moves:
                        winner = False
                if winner:
                    if Char is self.BotNumOne['Turn']:
                        self.Winner = self.BotNumOne['Name']
                        self.IsGameEnded = True
                        break
                    elif Char is self.BotNumTwo['Turn']:
                        self.Winner = self.BotNumTwo['Name']
                        self.IsGameEnded = True
                        break
        Items = len([Item for Item, Value in enumerate(self.GameBoard) if Value is not Empty])
        if Items is 9 and self.Winner is Empty:
            self.Winner = 'Draw'
            self.IsGameEnded = True

    # ---------------------------------
    # help region setters and getters

    # set BotOneName
    def SetBotOneName(self, Name):
        self.BotNumOne['Name'] = Name

    # set BotOneTwo
    def SetBotTwoName(self, Name):
        self.BotNumTwo['Name'] = Name

    # end of help region
    # ---------------------------------
