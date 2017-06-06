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






allStates = BoardState.calculateAllStates(BlackChess)

allStates = list(allStates)
print len(allStates)

worker = Worker()



