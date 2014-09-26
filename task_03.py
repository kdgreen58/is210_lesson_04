#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""My Task 3 code."""

import data

MAXIMUM = None
MINIMUM = None
DAYS = 0
TOTAL = 0

for DAY in data.TRANSACTIONS:
    DAYS += 1
    DAYTOTAL = 0
    for TRANS in DAY:
        DAYTOTAL += TRANS

    if DAYTOTAL < MINIMUM or MINIMUM is None:
        print "MIN CHANGE", MINIMUM, DAYTOTAL
        MINIMUM = DAYTOTAL
    if DAYTOTAL > MAXIMUM or MAXIMUM is None:
        print "MAX CHANGE", MAXIMUM, DAYTOTAL
        MAXIMUM = DAYTOTAL

    TOTAL += DAYTOTAL
