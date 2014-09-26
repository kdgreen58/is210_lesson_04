#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 5 Code"""

import data

MATCHUPS = ''
COUNTER = 0
LINE = '{0},"{1}","{2}"\n'

for ROW_INDEX, ROW_NAME in enumerate(data.VERSUS):
    for COLUMN_INDEX, COLUMN_NAME in enumerate(data.VERSUS):
        if ROW_INDEX < COLUMN_INDEX:
            COUNTER += 1
            MATCHUPS += LINE.format(COUNTER, COLUMN_NAME, ROW_NAME)

print MATCHUPS.strip("\n")
