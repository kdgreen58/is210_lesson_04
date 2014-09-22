#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A for loop for a Shakespeare play."""

import data

print data.SHAKESPEARE


RAWDATA = data.SHAKESPEARE.split("\n")

MAXIMUM_WORDS = None

for number in range(0, len(RAWDATA)):
    RAWDATAT = len(RAWDATA[number].split(" "))
    if RAWDATAT > MAXIMUM_WORDS:
        MAXIMUM_WORDS = RAWDATAT

MINIMUM_WORDS = MAXIMUM_WORDS

for numbertwo in range(0, len(RAWDATA)):
    RAWDATATT = len(RAWDATA[numbertwo].split(" "))
    if RAWDATATT < MINIMUM_WORDS:
        MINIMUM_WORDS = RAWDATATT

AVERAGE_WORDS = float(len(data.SHAKESPEARE.split())) / float(len(RAWDATA))

DATAREMOVE = data.SHAKESPEARE.replace(".", " ").replace("'", " ").replace(";",
    " ").replace("-", " ").replace("?", " ").replace(",", " ")
print DATAREMOVE
RAWDATATWO = DATAREMOVE.split()
NUM_CRISPIAN = RAWDATATWO.count("Crispian")
