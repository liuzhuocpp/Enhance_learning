def check3(a, b, c):
    return (a[0] - b[0] ) * (a[1] - c[1]) == (a[1] - b[1]) * (a[0] - c[0])

def check3(posList):
    n = len(posList)
    for i in xrange(n):
        for j in xrange(i + 1, n):
            for k in xrange(j + 1, n):
                if check3(posList[i], posList[j], posList[k]):
                    return True
    return False





def R(state, PieceType):
    this = []
    other = []
    for i in xrange(len(state)):
        if state[i][0] == PieceType:
            this.append(state[i][1], state[i][2])
        else:
            other.append(state[i][1], state[i][2])
    if check3(this):
        return 1.0
    elif check3(other):
        return 0.0
    else:
        return 0.5



#每个tuple的第0个元素是下一个动作
# key:tuple, value: Q
Q = {}
# key:tuple, value: count
count = {}
# Q[((BlackPiece, 0, 1), (WhitePiece, 3, 3), (WhitePiece, 3, 1))] = 0
# count[((BlackPiece, 0, 1), (WhitePiece, 3, 3), (WhitePiece, 3, 1))] = 0

def initQandCount(startPieceType):    
    for x in xrange(N):
        for y in xrange(N):                
            Q[(startPieceType, x, y)] = 0.0
            count[(startPieceType, x, y)] = 0



#一个state是一个tuple，tuple中每个元素是一个三元组tuple
def checkXY(state, x, y):
    for t, cx, cy in state:
        if cx == x and cx == y:
            return True
    return False




def argMaxQ(state, nextPieceType):
    opAnsPos = ()
    ansPos = ()
    maxQ = -1
    for x in xrange(N):
        for y in xrange(N):
            newState = (nextPieceType, x, y) + state
            if Q.has_key(newState) :
                if Q[newState] > maxQ:
                    maxQ = Q[newState]
                    ansPos = newState
            else:
                if not checkXY(state, x, y):
                    opAnsPos = newState

    if maxQ >= 0:
        return ansPos
    else:
        Q[opAnsPos] = 0.0
        count[opAnsPos] = 0
        return opAnsPos





# def epsilonGreedy(T, eps, initPieceType):
#     cntState = ()


#     for t in xrange(T):
#         nextAction = ()
#         if random.random() < eps:
#             k = random.randint(1, N * N - len(cntState))
#             cntk = 0

#             for x in xrange(N):
#                 for y in xrange(N):
#                     if ((WhitePiece, x, y) in cntState) or ((BlackPiece, x, y) in cntState):
#                         pass
#                     else:
#                         if cntk == k:
#                             nextAction = (initPieceType, x, y)
#                             break
#                         cntk += 1
#         else:
#             nextAction = argMaxQ(cntState, initPieceType)

#         if len(nextAction) == 0  :
#             break

#         nextState = nextAction + cntState
#         v = R(nextState, initPieceType)
#         Q[nextState] = (Q(nextState) * count(nextState) + v) / (count(nextState) + 1)
#         count[nextState] += 1




#         if initPieceType == WhitePiece:
#             initPieceType = BlackPiece
#         else:
#             initPieceType = WhitePiece


# for t  in xrange(100):
#     epsilonGreedy(25, 0.1, BlackPiece)

