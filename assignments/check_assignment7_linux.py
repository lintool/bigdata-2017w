#!/usr/bin/python
"""CS 489 Big Data Infrastructure (Winter 2017): Self-check script

This file can be open to students

Usage:
    run this file on 'bigdata2017w' repository with github-username
    ex) check_assignment7_public_linux.py [github-username]
"""

import sys,os,re,argparse
from subprocess import call

def check_a7(username,reducers):
    """Run assignment7 in linux environment"""
    call(["mvn","clean","package"])
    call(["hadoop","jar","target/bigdata2017w-0.1.0-SNAPSHOT.jar",
          "ca.uwaterloo.cs.bigdata2017w.assignment7.BuildInvertedIndexHBase",
          "-config", "/u0/cs489/hbase-site.xml",
          "-input", "data/Shakespeare.txt",
          "-index", "cs489-2017w-{0}-a7-index-shakespeare".format(username),
          "-reducers", str(reducers)])
    call(["hadoop","jar","target/bigdata2017w-0.1.0-SNAPSHOT.jar",
          "ca.uwaterloo.cs.bigdata2017w.assignment7.InsertCollectionHBase",
          "-config", "/u0/cs489/hbase-site.xml",
          "-input", "data/Shakespeare.txt",
          "-index", "cs489-2017w-{0}-a7-collection-shakespeare".format(username),
          "-reducers", str(reducers)])
    call(["hadoop","jar","target/bigdata2017w-0.1.0-SNAPSHOT.jar",
          "ca.uwaterloo.cs.bigdata2017w.assignment7.BooleanRetrievalHBase",
          "-config", "/u0/cs489/hbase-site.xml",
          "-index", "cs489-2017w-{0}-a7-index-shakespeare".format(username),
          "-collection", "cs489-2017w-{0}-a7-collection-shakespeare".format(username),
          "-query", "outrageous fortune AND"])


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="CS 489/689 2017w assignment public check script for Linux")
  parser.add_argument('username',metavar='[Github Username]', help="Github username",type=str)
  parser.add_argument('-r','--reducers',help="Number of reducers to use.",type=int,default=1)
  args=parser.parse_args()
  try:
    check_a7(args.username,args.reducers)
  except Exception as e:
    print(e)
