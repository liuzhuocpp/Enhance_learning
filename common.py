# -*- coding: UTF-8 -*-


#棋盘长度
N = 3

#连续多少个相同子获胜
WinLength = 3





Offset = 50            
Gap = 50

EmptyChess = 0
BlackChess = 1
WhiteChess = 2


def oppositeChess(chess):
    assert(chess != EmptyChess)
    if chess == BlackChess:
        return WhiteChess
    else:
        return BlackChess
        
def makeChess(pieceType, x, y):
    return (pieceType, x, y)
