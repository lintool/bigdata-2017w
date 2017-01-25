#!/usr/bin/python
"""CS 489 Big Data Infrastructure (Winter 2017): Self-check script

This file can be open to students

Usage: 
    run this file on 'bigdata2017w' repository with github-username
    ex) check_assignment3_public_linux.py [github-username]
"""

import sys,os,re,argparse
from subprocess import call

def check_a3(username,reducers):
    """Run assignment3 in linux environment"""
    call(["mvn","clean","package"])
    call(["hadoop","jar","target/bigdata2017w-0.1.0-SNAPSHOT.jar",
          "ca.uwaterloo.cs.bigdata2017w.assignment3.BuildInvertedIndexCompressed".format(username),
          "-input", "data/Shakespeare.txt", 
          "-output", "cs489-2017w-{0}-a3-index-shakespeare".format(username), "-reducers", str(reducers) ])
    print("\n\nQuestion 1.")
    call(["du","-h","cs489-2017w-{0}-a3-index-shakespeare".format(username)])
    print("\n\n")
    call(["hadoop","jar","target/bigdata2017w-0.1.0-SNAPSHOT.jar",
          "ca.uwaterloo.cs.bigdata2017w.assignment3.BooleanRetrievalCompressed".format(username),
          "-index","cs489-2017w-{0}-a3-index-shakespeare".format(username),
          "-collection","data/Shakespeare.txt","-query", "outrageous fortune AND"])
    call(["hadoop","jar","target/bigdata2017w-0.1.0-SNAPSHOT.jar",
          "ca.uwaterloo.cs.bigdata2017w.assignment3.BooleanRetrievalCompressed".format(username),
          "-index", "cs489-2017w-{0}-a3-index-shakespeare".format(username), 
          "-collection","data/Shakespeare.txt",
          "-query", "white red OR rose AND pluck AND"])

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="CS 489/689 2017w assignment public check script for Linux")
  parser.add_argument('username',metavar='[Github Username]', help="Github username",type=str)
  parser.add_argument('-r','--reducers',help="Number of reducers to use.",type=int,default=1)
  args=parser.parse_args()
  try:
    check_a3(args.username,args.reducers)
  except Exception as e:
    print(e)
