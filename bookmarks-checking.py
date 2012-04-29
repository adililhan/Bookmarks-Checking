#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Adil Ilhan"
import re
import urllib
import sys
import os

files = sys.argv
filesCount = len(files)

if filesCount != 2:
    sys.exit("Please, specify a file name.")
else:
    if os.path.exists(files[1]):
        initalize = open(files[1], 'r').read()
        comp = re.compile("<A\sHREF=\"(http:\/\/.*?)\"", re.U|re.S|re.I)
        path = os.path.basename(files[1])
        filename = path.split('.')[0]
        match = comp.findall(initalize)
        for i in match:
            print "That site checking: " + i
            try:
                siteStatus = urllib.urlopen(i).getcode()
                if siteStatus != 301 and siteStatus != 200 and siteStatus != 201 and siteStatus != 302:
                        data = open(filename + 'Matches.txt', 'a')
                        data.write(i + "\n")
                        data.close()
            except IOError:
               data = open(filename + 'Matches.txt', 'a')
               data.write(i + "\n")
               data.close()
    else:
        sys.exit ("File not found.")

    if os.path.exists(filename + 'Matches.txt'):
        print "Please check that file: " + filename + 'Matches.txt'
    else:
        print "All works!"