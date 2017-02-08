#!/usr/bin/python
"""CS 489 Big Data Infrastructure (Winter 2017): Self-check script

This file can be open to students

Usage: 
    run this file on 'bigdata2017w' repository with github-username
    ex) check_assignment5_public_altiscale.py [github-username]
"""

import sys
import os
from subprocess import call
import re

# add prefix 'a' if github-username starts from a numeric character
def convertusername(u):
  return re.sub(r'^(\d+.*)',r'a\1',u)

def check_a5(u):
    """Run assignment5 in AltiScale environment"""
    call(["mvn","clean","package"])

    call([ "my-spark-submit", "--class", "ca.uwaterloo.cs.bigdata2017w."+u+".assignment5.Q1",
	   "--num-executors", "10", "--driver-memory", "2g", "--executor-memory", "2g",	
 	   "target/bigdata2017w-0.1.0-SNAPSHOT.jar", "--input", "/shared/cs489/data/TPC-H-10-TXT", "--date", "1996-01-01", "--text"])

    call([ "my-spark-submit", "--class", "ca.uwaterloo.cs.bigdata2017w."+u+".assignment5.Q1",
       "--num-executors", "10", "--driver-memory", "2g", "--executor-memory", "2g", 
       "target/bigdata2017w-0.1.0-SNAPSHOT.jar", "--input", "/shared/cs489/data/TPC-H-10-PARQUET", "--date", "1996-01-01", "--parquet"])

    call([ "my-spark-submit", "--class", "ca.uwaterloo.cs.bigdata2017w."+u+".assignment5.Q2",
	   "--num-executors", "10", "--driver-memory", "2g", "--executor-memory", "2g",	
 	   "target/bigdata2017w-0.1.0-SNAPSHOT.jar", "--input", "/shared/cs489/data/TPC-H-10-TXT", "--date", "1996-01-01", "--text"])

    call([ "my-spark-submit", "--class", "ca.uwaterloo.cs.bigdata2017w."+u+".assignment5.Q2",
       "--num-executors", "10", "--driver-memory", "2g", "--executor-memory", "2g", 
       "target/bigdata2017w-0.1.0-SNAPSHOT.jar", "--input", "/shared/cs489/data/TPC-H-10-PARQUET", "--date", "1996-01-01", "--parquet"])

    call([ "my-spark-submit", "--class", "ca.uwaterloo.cs.bigdata2017w."+u+".assignment5.Q3",
	   "--num-executors", "10", "--driver-memory", "2g", "--executor-memory", "2g",	
 	   "target/bigdata2017w-0.1.0-SNAPSHOT.jar", "--input", "/shared/cs489/data/TPC-H-10-TXT", "--date", "1996-01-01", "--text"])

    call([ "my-spark-submit", "--class", "ca.uwaterloo.cs.bigdata2017w."+u+".assignment5.Q3",
       "--num-executors", "10", "--driver-memory", "2g", "--executor-memory", "2g", 
       "target/bigdata2017w-0.1.0-SNAPSHOT.jar", "--input", "/shared/cs489/data/TPC-H-10-PARQUET", "--date", "1996-01-01", "--parquet"])

    call([ "my-spark-submit", "--class", "ca.uwaterloo.cs.bigdata2017w."+u+".assignment5.Q4",
	   "--num-executors", "10", "--driver-memory", "2g", "--executor-memory", "2g",	
 	   "target/bigdata2017w-0.1.0-SNAPSHOT.jar", "--input", "/shared/cs489/data/TPC-H-10-TXT", "--date", "1996-01-01", "--text"])

    call([ "my-spark-submit", "--class", "ca.uwaterloo.cs.bigdata2017w."+u+".assignment5.Q4",
       "--num-executors", "10", "--driver-memory", "2g", "--executor-memory", "2g", 
       "target/bigdata2017w-0.1.0-SNAPSHOT.jar", "--input", "/shared/cs489/data/TPC-H-10-PARQUET", "--date", "1996-01-01", "--parquet"])

    call([ "my-spark-submit", "--class", "ca.uwaterloo.cs.bigdata2017w."+u+".assignment5.Q5",
	   "--num-executors", "10", "--driver-memory", "2g", "--executor-memory", "2g",	
 	   "target/bigdata2017w-0.1.0-SNAPSHOT.jar", "--input", "/shared/cs489/data/TPC-H-10-TXT", "--text"])

    call([ "my-spark-submit", "--class", "ca.uwaterloo.cs.bigdata2017w."+u+".assignment5.Q5",
       "--num-executors", "10", "--driver-memory", "2g", "--executor-memory", "2g", 
       "target/bigdata2017w-0.1.0-SNAPSHOT.jar", "--input", "/shared/cs489/data/TPC-H-10-PARQUET", "--parquet"])

    call([ "my-spark-submit", "--class", "ca.uwaterloo.cs.bigdata2017w."+u+".assignment5.Q6",
	   "--num-executors", "10", "--driver-memory", "2g", "--executor-memory", "2g",	
 	   "target/bigdata2017w-0.1.0-SNAPSHOT.jar", "--input", "/shared/cs489/data/TPC-H-10-TXT", "--date", "1996-01-01", "--text"])

    call([ "my-spark-submit", "--class", "ca.uwaterloo.cs.bigdata2017w."+u+".assignment5.Q6",
       "--num-executors", "10", "--driver-memory", "2g", "--executor-memory", "2g", 
       "target/bigdata2017w-0.1.0-SNAPSHOT.jar", "--input", "/shared/cs489/data/TPC-H-10-PARQUET", "--date", "1996-01-01", "--parquet"])

    call([ "my-spark-submit", "--class", "ca.uwaterloo.cs.bigdata2017w."+u+".assignment5.Q7",
	   "--num-executors", "10", "--driver-memory", "2g", "--executor-memory", "2g",	
 	   "target/bigdata2017w-0.1.0-SNAPSHOT.jar", "--input", "/shared/cs489/data/TPC-H-10-TXT", "--date", "1996-01-01", "--text"])

    call([ "my-spark-submit", "--class", "ca.uwaterloo.cs.bigdata2017w."+u+".assignment5.Q7",
       "--num-executors", "10", "--driver-memory", "2g", "--executor-memory", "2g", 
       "target/bigdata2017w-0.1.0-SNAPSHOT.jar", "--input", "/shared/cs489/data/TPC-H-10-PARQUET", "--date", "1996-01-01", "--parquet"])

if __name__ == "__main__":
  try:
    if len(sys.argv) < 2:
        print "usage: "+sys.argv[0]+" [github-username]"
        exit(1)
    u = convertusername(sys.argv[1])
    check_a5(u)
  except Exception as e:
    print(e)