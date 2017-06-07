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


FirstWin = 0
DrawChessboard = 1
FirstLose = 2
NotEnd = 3




FirstChessType = BlackChess


def oppositeChess(chess):
    assert(chess != EmptyChess)
    if chess == BlackChess:
        return WhiteChess
    else:
        return BlackChess

def makeChess(pieceType, x, y):
    return (pieceType, x, y)

# x 是虚拟坐标
def realCor(x):
    return  x * Gap + Offset

# x 是真实坐标
def imageCor(x):
    x -= Offset
    ans = x / Gap
    if x % Gap >= Gap / 2:
        ans += 1
    return ans

def isValidPos(x, y):
    return x >= 0 and x < N and y >= 0 and y < N
