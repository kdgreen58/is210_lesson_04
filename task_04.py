#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 4 code."""

import data

MAX = 12
COUNTER = 0
TEAM1 = ""
TEAM2 = ""
TEAM3 = ""

for LINE in data.MULTIPLAYERS.split("\n")[1:]:
    PLAYER_DATA = LINE.split()
    CONNECTION = int(PLAYER_DATA[1])
    NAME = PLAYER_DATA[0]

    if CONNECTION:
        COUNTER += 1
        TEAMID = COUNTER % 3
        if TEAMID == 1:
            TEAM1 += NAME + ","
        elif TEAMID == 2:
            TEAM2 += NAME + ","
        else:
            TEAM3 += NAME + ","           
    if COUNTER >= MAX:
        break

TEAM1 = TEAM1.rstrip(",")
TEAM2 = TEAM2.rstrip(",")
TEAM3 = TEAM3.rstrip(",")
