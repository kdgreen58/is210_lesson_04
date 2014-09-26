#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A for loop for a Shakespeare play."""

import data

print data.SHAKESPEARE


RAWDATA = data.SHAKESPEARE.split("\n")

MAXIMUM_WORDS = None

for NUMBER in range(0, len(RAWDATA)):
    RAWDATAT = len(RAWDATA[NUMBER].split(" "))
    if RAWDATAT > MAXIMUM_WORDS:
        MAXIMUM_WORDS = RAWDATAT

MINIMUM_WORDS = MAXIMUM_WORDS

for NUMBERTWO in range(0, len(RAWDATA)):
    RAWDATATT = len(RAWDATA[NUMBERTWO].split(" "))
    if RAWDATATT < MINIMUM_WORDS:
        MINIMUM_WORDS = RAWDATATT
        
AVERAGE_WORDS = float(len(data.SHAKESPEARE.split())) / float(len(RAWDATA))

COUNTER = 0
NUM_CRISPIAN = 0

for NUMBERTHREE in RAWDATA:
    COUNTER += 1
    if "Crispian" in NUMBERTHREE:
        NUM_CRISPIAN +=1
    
    

