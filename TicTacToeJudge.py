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


class TicTacToeJudge:
    # ini the game attributes
    def __init__(self, BotNumOneObj, BotNumTwoObj):
        self.GameBoard = [None, None, None, None, None, None, None, None, None]
        self.BotNumOne = {'Name': None, 'Turn': None, 'Char': None, 'Play': BotNumOneObj}
        self.BotNumTwo = {'Name': None, 'Turn': None, 'Char': None, 'Play': BotNumTwoObj}
        # In Tic-Tac-Toe there's 8 possible winning positions
        # across the top, across the middle, across the bottom,
        #  down the left side, down the middle, down the right side,
        # 45 diagonal and 135 diagonal /\
        self.WinningStates = ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6])
        self.BotTurn = 1
        self.IsGameEnded = False
        self.Winner = None

    # Randomly choose which bot to start the game
    def GoFirst(self):
        if random.randint(1, 2) == 1:
            self.BotNumOne['Turn'] = 1
            self.BotNumTwo['Turn'] = 2
            self.BotNumOne['Char'] = 'X'
            self.BotNumTwo['Char'] = 'O'
        else:
            self.BotNumTwo['Turn'] = 1
            self.BotNumOne['Turn'] = 2
            self.BotNumTwo['Char'] = 'X'
            self.BotNumOne['Char'] = 'O'

    # place the player's move on the board
    def MakeMove(self, char, position):
        if self.GameBoard[position] is None:
            self.GameBoard[position] = char
        else:
            self.TakeTurns()

    # place the player's moves while the game not ended
    def TakeTurns(self):
        if all(item is None for item in self.GameBoard):
            self.GoFirst()
        while not self.IsGameEnded:
            if self.BotNumOne['Turn'] is self.BotTurn:
                position = self.BotNumOne['Play'].play(self.GameBoard, self.BotNumOne['Char'])
                self.MakeMove(self.BotNumOne['Char'], position)
                self.BotTurn = self.BotNumTwo['Turn']
                self.IsWinner()
            elif self.BotNumTwo['Turn'] is self.BotTurn:
                position = self.BotNumTwo['Play'].play(self.GameBoard, self.BotNumTwo['Char'])
                self.MakeMove(self.BotNumTwo['Char'], position)
                self.BotTurn = self.BotNumOne['Turn']
                self.IsWinner()
        return self.Winner, self.GameBoard

    def IsWinner(self):
        for Char in (self.BotNumOne['Char'], self.BotNumTwo['Char']):
            Moves = [Move for Move, Value in enumerate(self.GameBoard) if Value == Char]
            for WinningState in self.WinningStates:
                winner = True
                for Move in WinningState:
                    if Move not in Moves:
                        winner = False
                if winner:
                    if Char is self.BotNumOne['Char']:
                        self.Winner = self.BotNumOne['Name']
                        self.IsGameEnded = True
                        break
                    elif Char is self.BotNumTwo['Char']:
                        self.Winner = self.BotNumTwo['Name']
                        self.IsGameEnded = True
                        break
        Items = len([Item for Item, Value in enumerate(self.GameBoard) if Value is not None])
        if Items is 9 and self.Winner is None:
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
