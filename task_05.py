#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 5 Code"""

import data

MATCHUPS = ""
COUNTER = 0
LINE = '{0},"{1}","{2}"\n'

for ROW_INDEX, ROW in enumerate(data.VERSUS):
    for COLUMN_INDEX, COLUMN in enumerate(data.VERSUS):
        if ROW_INDEX < COLUMN_INDEX:
            COUNTER += 1
            MATCHUPS += LINE.format(COUNTER, COLUMN, ROW)

print MATCHUPS.strip()
