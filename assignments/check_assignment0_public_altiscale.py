#!/usr/bin/python
"""CS 489 Big Data Infrastructure (Winter 2017): Self-check script

This file can be open to students

Usage:
    run this file on 'bigdata2017w' repository with github-username
    ex) check_assignment0_public_linux.py [github-username]
"""

import sys
import os
from subprocess import call
import re

def check_a0(u):
  """Run assignment0 in linux environment"""
  call(["mvn", "clean", "package"])
  call(["hadoop", "jar", "target/bigdata2017w-0.1.0-SNAPSHOT.jar",
        "ca.uwaterloo.cs.bigdata2017w.assignment0.PerfectX",
        "-input", "/shared/cs489/data/enwiki-20161220-sentences-0.1sample.txt",
        "-output", "cs489-2017w-"+u+"-a0-wiki" ])
  print("Question 5.")
  call("hadoop fs -cat cs489-2017w-"+u+"-a0-wiki/part* | sort -k 2 -n -r | head -10",shell=True)

if __name__ == "__main__":
  try:
    if len(sys.argv) < 2:
        print "usage: "+sys.argv[0]+" [github-username]"
        exit(1)
    check_a0(sys.argv[1])
  except Exception as e:
    print(e)
