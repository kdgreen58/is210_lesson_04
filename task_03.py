#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""My Task 3 code."""

import data

MAX = None
MIN = None
DAYS = 0
TOTAL = 0

for DAY in data.TRANSACTIONS:
    DAYS += 1
    DAYTOTAL = 0
    for TRANS in DAY:
        DAYTOTAL += TRANS

    if DAYTOTAL < MIN or MIN is None:
        print "MIN CHANGE", MIN, DAYTOTAL
        MIN = DAYTOTAL
    if DAYTOTAL > MAX or MAX is None:
        print "MAX CHANGE", MAX, DAYTOTAL
        MAX = DAYTOTAL

    TOTAL += DAYTOTAL
