#!/usr/bin/python
# -*- coding: UTF-8 -*-



import Tkinter
import random
from Tkinter import *


import tkMessageBox
import copy


from board_state import *
from common import *
from board_window import *
from worker import *

# class Worker:
#     def playChessHandler(self, event):
#         x , y = event.x, event.y
#         print "clicked at", x, y

#         x = imageCor(x)
#         y = imageCor(y)

#         if isValidPos(x, y) :
#             # global currentPieceType, boardState
#             # print "FFF"
#             chess = makeChess(self.currentPieceType, x, y)
#             if not self.boardState.isContain(x, y):
#                 # print "FFFddd"

#                 self.boardWindow.drawPiece(x, y, self.currentPieceType)
#                 # print "check win before: " , x, y
#                 if self.boardState.checkWin(self.currentPieceType, x, y):
#                     if self.currentPieceType == WhiteChess:
#                         tkMessageBox.showinfo(title='aaa', message='白棋获胜')
#                     else:
#                         tkMessageBox.showinfo(title='aaa', message='黑棋获胜')

#                 if self.boardState.getChessNumber() + 1 == N * N:
#                     tkMessageBox.showinfo(title='aaa', message='平局')
#                 self.boardState.playChess(chess)
#                 self.currentPieceType  = oppositeChess(self.currentPieceType)
 
#     def __init__(self):
#         self.boardWindow = BoardWindow()
#         self.boardState = BoardState()
#         self.currentPieceType = FirstChessType

#         self.boardWindow.frame.bind("<Button-1>", self.playChessHandler)
#         Button(self.boardWindow.frame, text='Hello Button', command= self.reset).grid(row = 0, column = 0)

#         self.boardWindow.drawBoard()

#     def reset(self):
#         self.boardWindow.reset()
#         self.boardState.clear()
#         self.currentPieceType = FirstChessType





allStates = BoardState.calculateAllStates(BlackChess)

allStates = list(allStates)
print len(allStates)

worker = Worker()



