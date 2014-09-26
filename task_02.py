#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 2 code."""

import data

ACCESS = False
COUNT = 4

while not ACCESS:
    COUNT -= 1
    MESSAGE = "What is your password? ({0} attempts left)?".format(COUNT)
    PASSWORD = raw_input(MESSAGE)
    if COUNT <= 1:
        print "Access is denied, please try again later."
        break
    if data.PASSWORD == PASSWORD:
        ACCESS = True
        print "Access Granted!!"
