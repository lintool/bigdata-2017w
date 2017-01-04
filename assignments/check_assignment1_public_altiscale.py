#!/usr/bin/python
"""CS 489 Big Data Infrastructure (Winter 2017): Self-check script

This file can be open to students

Usage: 
    run this file on 'bigdata2017w' repository with github-username
    ex) check_assignment1_public_altiscale.py [github-username]
"""

import sys
import os
from subprocess import call
import re

def check_a1(u):
  """Run assignment1 in linux environment"""
  call(["mvn","clean","package"])

  call([ "hadoop","jar","target/bigdata2017w-0.1.0-SNAPSHOT.jar",
         "ca.uwaterloo.cs.bigdata2017w.assignment1.PairsPMI",
         "-input", "/shared/cs489/data/simplewiki-20161220-sentences.txt", 
         "-output", "cs489-2017w-"+u+"-a1-wiki-pairs", "-reducers", "5", "-threshold", "50"])
  call([ "hadoop","jar","target/bigdata2017w-0.1.0-SNAPSHOT.jar",
         "ca.uwaterloo.cs.bigdata2017w.assignment1.StripesPMI",
         "-input", "/shared/cs489/data/enwiki-20151201-pages-articles-0.1sample.txt", 
         "-output", "cs489-2017w-"+u+"-a1-wiki-stripes", "-reducers", "5", "-threshold", "50"])
  print("\n\nQuestion 7.")
  call("hadoop fs -cat cs489-2017w-"+u+"-a1-wiki-pairs/part-r-0000* | grep '(hockey,' | sort -t'(' -k 3 -n -r | head -5",shell=True)
  print("\n\nQuestion 8.")
  call("hadoop fs -cat cs489-2017w-"+u+"-a1-wiki-pairs/part-r-0000* | grep '(data,' | sort -t'(' -k 3 -n -r | head -5",shell=True)
  print("");
	
if __name__ == "__main__":
  try:
    if len(sys.argv) < 2:
        print "usage: "+sys.argv[0]+" [github-username]"
        exit(1)
    check_a1(sys.argv[1])
  except Exception as e:
    print(e)
