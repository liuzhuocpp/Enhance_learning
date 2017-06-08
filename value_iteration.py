#coding: UTF-8


from board_state import *

from common import *
import copy
import math

def R(boardState, selfChessType = FirstChessType):

    situation = boardState.checkFirstSituatoin()
    if situation == FirstWin:
        return 1.0
    elif situation == FirstLose:
        return 0.0
    elif situation == DrawChessboard:
        return 0.0
    elif situation == NotEnd:
        return 0.5
    else:
        assert(False)






def valueIterate(T, delta):

    watchedState = BoardState()
    watchedState.playChess(makeChess(BlackChess, 0, 0))
    watchedState.playChess(makeChess(BlackChess, 0, 1))
    watchedState.playChess(makeChess(WhiteChess, 0, 2)) 

    # watchedState.playChess(makeChess(WhiteChess, 1, 0))
    # watchedState.playChess(makeChess(BlackChess, 1, 1))
    watchedState.playChess(makeChess(BlackChess, 1, 2))

    watchedState.playChess(makeChess(WhiteChess, 2, 0))
    watchedState.playChess(makeChess(WhiteChess, 2, 1))       
    # watchedState.playChess(makeChess(WhiteChess, 2, 2))



    allStates = BoardState.calculateAllStates()
    policy = {}
    V = {}
    for s in allStates:
        V[s] = 0.0        

    policyModifiedNumber = 0


    t = 1.0
    while True:
        print "GG"
        _V = {}
        maxDiff = 0.0
        for s in allStates:

            if s.isEnd():
                _V[s] = 0.0
                continue

            _V[s] = -111.0
            s_policy = None
            for x in xrange(N):
                for y in xrange(N):
                    if  s.isContain(x, y): continue
                    nextChess = makeChess(FirstChessType, x, y)
                    nextState = BoardState.makeNewState(s, nextChess)

                    nextValueSum = 0.0
                    if nextState.isEnd():
                        nextValueSum = R(nextState)
                    else:
                        nextNextStateNum = 0
                        for nx in xrange(N):
                            for ny in xrange(N):
                                if nextState.isContain(nx, ny): continue

                                nextNextStateNum += 1
                                nextNextState = BoardState.makeNewState(nextState, makeChess(oppositeChess(FirstChessType), nx, ny))
                                if nextNextState.isEnd():
                                    nextValueSum += R(nextNextState)
                                else:
                                    nextValueSum += (R(nextNextState) + (t - 1) * V[nextNextState]) / t
                        if nextNextStateNum == 0:
                            assert(False)
                        nextValueSum /= nextNextStateNum

                    if _V[s] < nextValueSum:
                        _V[s] = nextValueSum

                        if s_policy == None or s_policy != nextChess:                            
                            s_policy = nextChess
                            


                                # if s == watchedState:
            if not policy.has_key(s) or policy[s] != s_policy:
                policy[s] = s_policy
                policyModifiedNumber+=1
                if policyModifiedNumber % 1000 == 0:
                    print 'policyModifiedNumber: ', policyModifiedNumber, _V[s]

                            

            if _V[s] < 0.0:
                print s, "jjjj"
                assert(False)

            maxDiff = max(maxDiff, math.fabs(_V[s] - V[s]))

        # print 'haha\n'
        # print watchedState, _V[watchedState], "\n"

        

        t += 1.0
        if maxDiff < delta:
            break
        else:
            V = _V
        # break

        print "max diff", maxDiff, t, V[watchedState]



    return policy





















# def check3(a, b, c):
#     return (a[0] - b[0] ) * (a[1] - c[1]) == (a[1] - b[1]) * (a[0] - c[0])

# def check3(posList):
#     n = len(posList)
#     for i in xrange(n):
#         for j in xrange(i + 1, n):
#             for k in xrange(j + 1, n):
#                 if check3(posList[i], posList[j], posList[k]):
#                     return True
#     return False





# def R(state, PieceType):
#     this = []
#     other = []
#     for i in xrange(len(state)):
#         if state[i][0] == PieceType:
#             this.append(state[i][1], state[i][2])
#         else:
#             other.append(state[i][1], state[i][2])
#     if check3(this):
#         return 1.0
#     elif check3(other):
#         return 0.0
#     else:
#         return 0.5



# #每个tuple的第0个元素是下一个动作
# # key:tuple, value: Q
# Q = {}
# # key:tuple, value: count
# count = {}
# # Q[((BlackPiece, 0, 1), (WhitePiece, 3, 3), (WhitePiece, 3, 1))] = 0
# # count[((BlackPiece, 0, 1), (WhitePiece, 3, 3), (WhitePiece, 3, 1))] = 0

# def initQandCount(startPieceType):    
#     for x in xrange(N):
#         for y in xrange(N):                
#             Q[(startPieceType, x, y)] = 0.0
#             count[(startPieceType, x, y)] = 0



# #一个state是一个tuple，tuple中每个元素是一个三元组tuple
# def checkXY(state, x, y):
#     for t, cx, cy in state:
#         if cx == x and cx == y:
#             return True
#     return False




# def argMaxQ(state, nextPieceType):
#     opAnsPos = ()
#     ansPos = ()
#     maxQ = -1
#     for x in xrange(N):
#         for y in xrange(N):
#             newState = (nextPieceType, x, y) + state
#             if Q.has_key(newState) :
#                 if Q[newState] > maxQ:
#                     maxQ = Q[newState]
#                     ansPos = newState
#             else:
#                 if not checkXY(state, x, y):
#                     opAnsPos = newState

#     if maxQ >= 0:
#         return ansPos
#     else:
#         Q[opAnsPos] = 0.0
#         count[opAnsPos] = 0
#         return opAnsPos





# # def epsilonGreedy(T, eps, initPieceType):
# #     cntState = ()


# #     for t in xrange(T):
# #         nextAction = ()
# #         if random.random() < eps:
# #             k = random.randint(1, N * N - len(cntState))
# #             cntk = 0

# #             for x in xrange(N):
# #                 for y in xrange(N):
# #                     if ((WhitePiece, x, y) in cntState) or ((BlackPiece, x, y) in cntState):
# #                         pass
# #                     else:
# #                         if cntk == k:
# #                             nextAction = (initPieceType, x, y)
# #                             break
# #                         cntk += 1
# #         else:
# #             nextAction = argMaxQ(cntState, initPieceType)

# #         if len(nextAction) == 0  :
# #             break

# #         nextState = nextAction + cntState
# #         v = R(nextState, initPieceType)
# #         Q[nextState] = (Q(nextState) * count(nextState) + v) / (count(nextState) + 1)
# #         count[nextState] += 1




# #         if initPieceType == WhitePiece:
# #             initPieceType = BlackPiece
# #         else:
# #             initPieceType = WhitePiece


# # for t  in xrange(100):
# #     epsilonGreedy(25, 0.1, BlackPiece)

