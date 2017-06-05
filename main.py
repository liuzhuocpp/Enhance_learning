#!/usr/bin/python
# -*- coding: UTF-8 -*-



import Tkinter
import random
from Tkinter import *
from common import *

import tkMessageBox
import copy


from board_state import *



def isValidPos(x, y):
    return x >= 0 and x < N and y >= 0 and y < N




        



currentPieceType = BlackChess
boardState = BoardState()


# x 是真实坐标
def imageCor(x):
    x -= Offset
    ans = x / Gap
    if x % Gap >= Gap / 2:
        ans += 1
    return ans

def playChessHandler(event):
    x , y = event.x, event.y
    print "clicked at", x, y

    x = imageCor(x)
    y = imageCor(y)

    if isValidPos(x, y) :
        global currentPieceType, boardState
        print "FFF"
        chess = makeChess(currentPieceType, x, y)
        if not boardState.isContain(x, y):
            print "FFFddd"

            chessboard.drawPiece(x, y, currentPieceType)
            print "check win before: " , x, y
            if boardState.checkWin(currentPieceType, x, y):

                if currentPieceType == WhiteChess:
                    tkMessageBox.showinfo(title='aaa', message='白棋获胜')
                else:
                    tkMessageBox.showinfo(title='aaa', message='黑棋获胜')

            if boardState.getChessNumber() + 1 == N * N:
                tkMessageBox.showinfo(title='aaa', message='平局')
            boardState.playChess(chess)

            currentPieceType  = oppositeChess(currentPieceType)



















frame = Tk()


def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Tkinter.Canvas.create_circle = _create_circle


canvas = Canvas(frame, width=800, height=800)

canvas.grid()

# x 是虚拟坐标
def realCor(x):
    return  x * Gap + Offset




class Chessboard:

    def clear(self):
        canvas.delete("all")

    def drawBoard(self):
        for y in xrange(0, N):
            canvas.create_line(realCor(0), realCor(y), realCor(N - 1), realCor(y), fill="red")
        for x in xrange(0, N):
            canvas.create_line(realCor(x), realCor(0),  realCor(x), realCor(N - 1), fill="red")
        # for x in xrange(0, N):
        #     for y in xrange(0, N):
        #         w.create_circle(realCor(x * gap), realCor(y * gap), 15,  fill="blue", outline="#DDD", width=4)

    def drawPiece(self, x, y, PieceType):
        if PieceType == BlackChess:
            canvas.create_circle(realCor(x), realCor(y), 15,  fill="black")
        elif PieceType == WhiteChess:
            canvas.create_circle(realCor(x ), realCor(y), 15,  fill="white")
        else:
            print "error"





chessboard = Chessboard()
chessboard.drawBoard()
# chessboard.drawPiece(0, 0, BlackPiece)
# chessboard.drawPiece(0, 1, WhitePiece)
def resetBoard():  
    chessboard.clear()
    chessboard.drawBoard()

    boardState.clear()
    global currentPieceType 
    currentPieceType = BlackChess

frame.bind("<Button-1>", playChessHandler)
Button(frame, text='Hello Button', command=resetBoard).grid(row = 0, column = 0)





allStates = BoardState.calculateAllStates(BlackChess)

allStates = list(allStates)
print len(allStates)

# def myCmp(x, y):
#     if x.state1 != y.state1:
#         return x.state1 - y.state1
#     return x.state2 - y.state2
# allStates.sort( cmp = myCmp)
# for v in allStates:
#     print v.state1, v.state2, "kkk"
#     print v.toChessTuple()



mainloop()






# class Test:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

# # def cmp1(a, b):
# #     if a.a != b.a:
# #         return a.a < 

# a = [Test(1, 2), Test(1, 3333), Test(3234234, 22), Test(1, 222)]
# a.sort()

# for x in a:
#     print x.a, x.b

