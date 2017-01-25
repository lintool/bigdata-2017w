#!/usr/bin/python
"""CS 489 Big Data Infrastructure (Winter 2017): Self-check script

This file can be open to students

Usage: 
    run this file on 'bigdata2017w' repository with github-username
    ex) check_assignment1_public_linux.py [github-username]
"""

import sys
import os
from subprocess import call
import re
import argparse

def check_a3(username,reducers):
    """Run assignment3 in Altiscale environment"""
    call(["mvn","clean","package"])
    print username
    call(["hadoop","jar","target/bigdata2017w-0.1.0-SNAPSHOT.jar",
          "ca.uwaterloo.cs.bigdata2017w.assignment3.BuildInvertedIndexCompressed".format(username),
          "-input", "/shared/cs489/data/enwiki-20161220-sentences-0.1sample.txt", 
          "-output", "cs489-2017w-{0}-a3-index-wiki".format(username), "-reducers", str(reducers) ])
    print("\n\nQuestion 2.\n")
    call(["hadoop","fs","-du","-h","cs489-2017w-{0}-a3-index-wiki".format(username)])
    print("\n\nQuestion 3.\n")
    call(["hadoop","jar","target/bigdata2017w-0.1.0-SNAPSHOT.jar",
          "ca.uwaterloo.cs.bigdata2017w.assignment3.BooleanRetrievalCompressed".format(username),
          "-index", "cs489-2017w-{0}-a3-index-wiki".format(username), 
          "-collection", "/shared/cs489/data/enwiki-20161220-sentences-0.1sample.txt",
          "-query", "waterloo stanford OR cheriton AND"])
    print("\n\nQuestion 4.\n")
    call(["hadoop","jar","target/bigdata2017w-0.1.0-SNAPSHOT.jar",
          "ca.uwaterloo.cs.bigdata2017w.assignment3.BooleanRetrievalCompressed".format(username),
          "-index", "cs489-2017w-{0}-a3-index-wiki".format(username),
          "-collection", "/shared/cs489/data/enwiki-20161220-sentences-0.1sample.txt",
          "-query", "big data AND hadoop spark OR AND"])

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="CS 489/689 2017w assignment public check script for Altiscale")
  parser.add_argument('username',metavar='[Github Username]', help="Github username",type=str)
  parser.add_argument('-r','--reducers',help="Number of reducers to use.",type=int,default=1)
  args=parser.parse_args()
  try:
    check_a3(args.username,args.reducers)
  except Exception as e:
    print(e)
