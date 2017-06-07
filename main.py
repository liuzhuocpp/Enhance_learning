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

from value_iteration import *













policy = valueIterate(N * N, 0.1)

# worker = Worker()
worker = MachineWorker(policy)



