"""
about:
This code was written by Mostafa El-Marzouki @iSuperMostafa
------------------------------------------------------------
summery:
this judge allows you to focus on choosing the best position to play
tic-tac-toe game Just by write your code in BotNumOne or BotNumTwo
"""
import TicTacToeJudge
import MinimaxBot, DummyBot

BotNumOneObj = MinimaxBot.BotNumOne()
BotNumTwoObj = DummyBot.BotNumTwo()
Judge = TicTacToeJudge.TicTacToeJudge(BotNumOneObj, BotNumTwoObj)
Judge.SetBotOneName("Bot One")
Judge.SetBotTwoName("Bot Two")
Winner, GameBaord = Judge.TakeTurns()
print(Winner)
for line in (GameBaord[iterator:iterator + 3] for iterator in range(0, len(GameBaord), 3)):
    print(str(line))
# print(GameBaord)
