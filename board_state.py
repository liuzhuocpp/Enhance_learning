#!/usr/bin/python
# -*- coding: UTF-8 -*-

from common import *
import copy
import numpy

class BoardState:

    def __init__(self):
        self.state1 = 0 # 一个三进制数字，0-for empty, 2-for black, 2 for white
        self.state2 = 0
    def __eq__(self, other):
        return self.state1 == other.state1 and self.state2 == other.state2
        # self.chessTuple= ()
    def __hash__(self):
        return ((self.state1 << (N * N)) + self.state2) &((1 << 32) - 1)

    def __str__(self):
        chessTuple = self.toChessTuple()
        out = numpy.zeros((N, N), )
        for chess in chessTuple :
            t, x, y = chess
            if t == WhiteChess:
                out[x][y] = 2
            elif t == BlackChess:
                out[x][y] = 1
            else:
                print 'error'
        return str(out)

    def getChessType(self, i, j):
        i = i * N + j
        if BoardState._getValue(self.state1, i):
            if BoardState._getValue(self.state2, i):
                return WhiteChess
            else:
                return BlackChess
        return EmptyChess

    #以state之中下一个chess的新的state
    @staticmethod
    def makeNewState(state, chess):
        state = copy.copy(state)
        state.playChess(chess)
        return state


    @staticmethod
    def _getValue(s, i):
        return (s >> i) & 1

    @staticmethod
    def _getSetValue(s, i, v):
        if BoardState._getValue(s, i) != v:
            return s ^ (1 << i)
        return s
        # for ii in xrange(i):
        #     s /= 3
        # return s % 3

    def getChessNumber(self):
        return len(self.toChessTuple())
    def setChess(self, i, j, v):
        i = i * N + j
        if v == EmptyChess:
            self.state1 = BoardState._getSetValue(self.state1, i, 0)
            self.state2 = BoardState._getSetValue(self.state2, i, 0)
        else:
            self.state1 = BoardState._getSetValue(self.state1, i, 1)
            if v == BlackChess:
                self.state2 = BoardState._getSetValue(self.state2, i, 0)
            else:
                self.state2 = BoardState._getSetValue(self.state2, i, 1)

    def clear(self):
        self.state1 = 0  
        self.state2 = 0

    def toChessTuple(self):
        ans = ()
        for i in xrange(N):
            for j in xrange(N):
                c = self.getChessType(i, j)
                if c != EmptyChess:
                    ans += ((c, i, j),) 

        return ans

    # def __str__(self):
    #     return self.toChessTuple()
    # 检查先手局面

    def checkFirstSituatoin(self):
        for x in xrange(N):
            for y in xrange(N):
                if self.isContain(x, y):
                    cntChessType = self.getChessType(x, y)
                    if self.checkWin((cntChessType, x, y)):
                        if cntChessType == FirstChessType:
                            return FirstWin
                        else:
                            return FirstLose
        if self.getChessNumber() == N * N:
            return DrawChessboard
        return NotEnd


    def isEnd(self):
        return self.checkFirstSituatoin() != NotEnd

    # 机器是先手
    @staticmethod
    def calculateAllStates():
        ans = set()
        # 局面状态，是否是一个边界状态
        q = [BoardState() ]

        def addState(state):
            if state not in ans:
                ans.add(state)


        while len(q) > 0:

            if len(ans) % 10000 == 0:
                print len(ans), len(q)

            cntState = q.pop()
            ans.add(cntState)
            if cntState.isEnd():
                continue
            for x in xrange(N):
                for y in xrange(N):
                    if cntState.isContain(x, y):  continue

                    nextState = BoardState.makeNewState(cntState, makeChess(FirstChessType, x, y))

                    if not nextState.isEnd():
                        for nx in xrange(N):
                            for ny in xrange(N):
                                if  nextState.isContain(nx, ny): continue
                                nextNextState = BoardState.makeNewState(nextState, makeChess(oppositeChess(FirstChessType), nx, ny))                                
                                if nextNextState not in ans:
                                    q.append(nextNextState)
                    else:
                        if nextState not in ans:
                            q.append(nextState)
        return ans




    @staticmethod
    def moveDirs():
        return [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),

        (1, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),]


    def isContain(self, qx , qy):

        v = self.getChessType(qx, qy)
        if v != EmptyChess:
            return True
        return False

    def playChess(self, chess):
        t, x, y = chess
        self.setChess(x, y, t)

    # def checkTie(self, chess):
    #     return len(self.toChessTuple()) + 1 == N * N

    def checkWin(self, chess):

        def maxLength(posList, x, y, nx, ny):
            ans = 0
            while True:
                x += nx
                y += ny
                if (x, y) not in posList:
                    break
                ans +=1
            return ans


        # 以x, y坐标为中心是否有长度达到k
        def checkMulti(posList, x, y, k):
            moveDirs = BoardState.moveDirs()


            # print "CAO",  maxLength(posList, x, y, 0, -1), "FFF", posList, "KKK", (x, y)

            for i in xrange(0, len(moveDirs), 2):
                maxL = maxLength(posList, x, y, moveDirs[i][0], moveDirs[i][1])
                antiMaxL = maxLength(posList, x, y, moveDirs[i + 1][0], moveDirs[i + 1][1])
                _sum = maxL + antiMaxL + 1
                # print "_SUM" , _sum, maxL, antiMaxL


                if _sum >= k:
                    return True
            return False



        thisPosList = []
        for t, tx, ty in self.toChessTuple():
            if t == chess[0]:
                thisPosList.append((tx, ty))

        return checkMulti(thisPosList, chess[1], chess[2], WinLength)
