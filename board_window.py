import Tkinter



from Tkinter import *
from common import *

class BoardWindow:

    @staticmethod
    def  _create_circle(self, x, y, r, **kwargs):
        return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)

    def __init__(self):
        Tkinter.Canvas.create_circle = BoardWindow._create_circle
        self.frame = Tk()
        self.canvas =  Canvas(self.frame, width=800, height=800)
        self.canvas.grid()
        
    def reset(self):
        self.canvas.delete("all")
        self.drawBoard()

    def clear(self):
        canvas.delete("all")

    def drawBoard(self):
        for y in xrange(0, N):
            self.canvas.create_line(realCor(0), realCor(y), realCor(N - 1), realCor(y), fill="red")
        for x in xrange(0, N):
            self.canvas.create_line(realCor(x), realCor(0),  realCor(x), realCor(N - 1), fill="red")
        # for x in xrange(0, N):
        #     for y in xrange(0, N):
        #         w.create_circle(realCor(x * gap), realCor(y * gap), 15,  fill="blue", outline="#DDD", width=4)

    def drawPiece(self, x, y, chessType):
        if chessType == BlackChess:
            self.canvas.create_circle(realCor(x), realCor(y), 15,  fill="black")
        elif chessType == WhiteChess:
            self.canvas.create_circle(realCor(x ), realCor(y), 15,  fill="white")
        else:
            print "error"






