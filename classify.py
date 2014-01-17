#!/usr/bin/python

import sys
import csv

def main():
  if not len(sys.argv) == 2:
    raise Exception("Classify takes in one csv file as argument")

  csvfilepath = sys.argv[1]
  csvfile = open('test.csv','rb')
  reader = csv.reader(csvfile)

  headers = []
  rowDicts = []
  rowNum = 0
  for r in reader:
    if rowNum == 0:
      headers = r
    else:
      rowDicts.append(rowToDictionary(headers,r))
    rowNum += 1

  selectedHeader = promptForHeader(headers)
  print("Selected header: " + selectedHeader)

  classify(rowDicts, selectedHeader)

def classify(rowDicts, key):
  buckets = {}
  bucket = []
  classCache = {}
  for rd in rowDicts:
    toClassify = rd[key]
    if toClassify in classCache:
      classifier = classCache[toClassify]
    else:
      print("How should I classify " + rd[key] + "? ")
      print("Current Classes: ")
      print(buckets.keys())
      classifier = raw_input("What do you think? ")
      classCache[toClassify] = classifier

    if classifier in buckets:
      bucket = buckets[classifier]
    else:
      bucket = []

    bucket.append(rd)
    buckets[classifier] = bucket

  print("PRINT buckets")
  print(buckets)

def promptForHeader(headers):
  for h in headers:
    response = raw_input("Classify by " + h  + "? (y/n) ")
    if response == "y":
      return h
  raise Exception("You must chose a classifier")

def rowToDictionary(keys, row):
  dict = {}
  i = 0
  for k in keys:
    dict[k] = row[i]
    i += 1

  print(dict)
  return dict

if __name__ == "__main__":
  main()

