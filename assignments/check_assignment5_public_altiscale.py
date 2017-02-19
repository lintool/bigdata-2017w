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

def check_a5(u):
    """Run assignment5 in AltiScale environment"""
    call(["mvn","clean","package"])

    with open("q1t.out", "w") as outfile:
        call(["a5-spark-submit", "--class", "ca.uwaterloo.cs.bigdata2017w.assignment5.Q1",
              "--num-executors", "5", "--executor-cores", "2", "--executor-memory", "4G", "--driver-memory", "2g",
              "target/bigdata2017w-0.1.0-SNAPSHOT.jar", "--input", "/shared/cs489/data/TPC-H-10-TXT",
              "--date", "1996-01-01", "--text"], stdout=outfile)

    with open("q1p.out", "w") as outfile:
        call(["a5-spark-submit", "--class", "ca.uwaterloo.cs.bigdata2017w.assignment5.Q1",
              "--num-executors", "5", "--executor-cores", "2", "--executor-memory", "4G", "--driver-memory", "2g",
              "target/bigdata2017w-0.1.0-SNAPSHOT.jar", "--input", "/shared/cs489/data/TPC-H-10-PARQUET",
              "--date", "1996-01-01", "--parquet"], stdout=outfile)

    with open("q2t.out", "w") as outfile:
        call(["a5-spark-submit", "--class", "ca.uwaterloo.cs.bigdata2017w.assignment5.Q2",
              "--num-executors", "5", "--executor-cores", "2", "--executor-memory", "4G", "--driver-memory", "2g",
              "target/bigdata2017w-0.1.0-SNAPSHOT.jar", "--input", "/shared/cs489/data/TPC-H-10-TXT",
              "--date", "1996-01-01", "--text"], stdout=outfile)

    with open("q2p.out", "w") as outfile:
        call(["a5-spark-submit", "--class", "ca.uwaterloo.cs.bigdata2017w.assignment5.Q2",
              "--num-executors", "5", "--executor-cores", "2", "--executor-memory", "4G", "--driver-memory", "2g",
              "target/bigdata2017w-0.1.0-SNAPSHOT.jar", "--input", "/shared/cs489/data/TPC-H-10-PARQUET",
              "--date", "1996-01-01", "--parquet"], stdout=outfile)

    with open("q3t.out", "w") as outfile:
        call(["a5-spark-submit", "--class", "ca.uwaterloo.cs.bigdata2017w.assignment5.Q3",
              "--num-executors", "5", "--executor-cores", "2", "--executor-memory", "4G", "--driver-memory", "2g",
              "target/bigdata2017w-0.1.0-SNAPSHOT.jar", "--input", "/shared/cs489/data/TPC-H-10-TXT",
              "--date", "1996-01-01", "--text"], stdout=outfile)

    with open("q3p.out", "w") as outfile:
        call(["a5-spark-submit", "--class", "ca.uwaterloo.cs.bigdata2017w.assignment5.Q3",
              "--num-executors", "5", "--executor-cores", "2", "--executor-memory", "4G", "--driver-memory", "2g",
              "target/bigdata2017w-0.1.0-SNAPSHOT.jar", "--input", "/shared/cs489/data/TPC-H-10-PARQUET",
              "--date", "1996-01-01", "--parquet"], stdout=outfile)

    with open("q4t.out", "w") as outfile:
        call(["a5-spark-submit", "--class", "ca.uwaterloo.cs.bigdata2017w.assignment5.Q4",
              "--num-executors", "5", "--executor-cores", "2", "--executor-memory", "4G", "--driver-memory", "2g",
              "target/bigdata2017w-0.1.0-SNAPSHOT.jar", "--input", "/shared/cs489/data/TPC-H-10-TXT",
              "--date", "1996-01-01", "--text"], stdout=outfile)

    with open("q4p.out", "w") as outfile:
        call(["a5-spark-submit", "--class", "ca.uwaterloo.cs.bigdata2017w.assignment5.Q4",
              "--num-executors", "5", "--executor-cores", "2", "--executor-memory", "4G", "--driver-memory", "2g",
              "target/bigdata2017w-0.1.0-SNAPSHOT.jar", "--input", "/shared/cs489/data/TPC-H-10-PARQUET",
              "--date", "1996-01-01", "--parquet"], stdout=outfile)

    with open("q5t.out", "w") as outfile:
        call(["a5-spark-submit", "--class", "ca.uwaterloo.cs.bigdata2017w.assignment5.Q5",
              "--num-executors", "5", "--executor-cores", "2", "--executor-memory", "4G", "--driver-memory", "2g",
              "target/bigdata2017w-0.1.0-SNAPSHOT.jar", "--input", "/shared/cs489/data/TPC-H-10-TXT", "--text"], stdout=outfile)

    with open("q5p.out", "w") as outfile:
        call(["a5-spark-submit", "--class", "ca.uwaterloo.cs.bigdata2017w.assignment5.Q5",
              "--num-executors", "5", "--executor-cores", "2", "--executor-memory", "4G", "--driver-memory", "2g",
              "target/bigdata2017w-0.1.0-SNAPSHOT.jar", "--input", "/shared/cs489/data/TPC-H-10-PARQUET", "--parquet"], stdout=outfile)

    with open("q6t.out", "w") as outfile:
        call(["a5-spark-submit", "--class", "ca.uwaterloo.cs.bigdata2017w.assignment5.Q6",
              "--num-executors", "5", "--executor-cores", "2", "--executor-memory", "4G", "--driver-memory", "2g",
              "target/bigdata2017w-0.1.0-SNAPSHOT.jar", "--input", "/shared/cs489/data/TPC-H-10-TXT",
              "--date", "1996-01-01", "--text"], stdout=outfile)

    with open("q6p.out", "w") as outfile:
        call(["a5-spark-submit", "--class", "ca.uwaterloo.cs.bigdata2017w.assignment5.Q6",
              "--num-executors", "5", "--executor-cores", "2", "--executor-memory", "4G", "--driver-memory", "2g",
              "target/bigdata2017w-0.1.0-SNAPSHOT.jar", "--input", "/shared/cs489/data/TPC-H-10-PARQUET",
              "--date", "1996-01-01", "--parquet"], stdout=outfile)

    with open("q7t.out", "w") as outfile:
        call(["a5-spark-submit", "--class", "ca.uwaterloo.cs.bigdata2017w.assignment5.Q7",
              "--num-executors", "5", "--executor-cores", "2", "--executor-memory", "4G", "--driver-memory", "2g",
              "target/bigdata2017w-0.1.0-SNAPSHOT.jar", "--input", "/shared/cs489/data/TPC-H-10-TXT",
              "--date", "1996-01-01", "--text"], stdout=outfile)

    with open("q7p.out", "w") as outfile:
        call(["a5-spark-submit", "--class", "ca.uwaterloo.cs.bigdata2017w.assignment5.Q7",
              "--num-executors", "5", "--executor-cores", "2", "--executor-memory", "4G", "--driver-memory", "2g",
              "target/bigdata2017w-0.1.0-SNAPSHOT.jar", "--input", "/shared/cs489/data/TPC-H-10-PARQUET",
              "--date", "1996-01-01", "--parquet"], stdout=outfile)


if __name__ == "__main__":
  try:
    if len(sys.argv) < 2:
        print "usage: "+sys.argv[0]+" [github-username]"
        exit(1)
    check_a5(sys.argv[1])
  except Exception as e:
    print(e)
