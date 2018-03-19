#!/usr/bin/env python

"""
FIND DUPLICATES IN APACHE ACCESS.LOG AND PRINT THEM TO FILE
DLScript by Alex Rodionov (p0deje@gmail.com)
"""

import re, sys

# Usage
if len(sys.argv) < 4:
  print """
Script parses Apache's access_log for specific method URL,
finds duplicate entries and sort them in the most frequent order.
Useful when you need to get all URLs from access_log.

Usage:
./script.py METHOD ORIGIN OUTPUT [REPETITION]

Parameters:
METHOD        which HTTP method to look for.
ORIGIN        original file to parse.
OUTPUT        output file to print to.
REPETITION    optional. If set, script prints number of occurence before URL.

Example:
./script.py GET access_log output_file TRUE
"""
  sys.exit()

# Get arguments
method = sys.argv[1]
access_log = sys.argv[2]
output_log = sys.argv[3]
# Files
original_file = open(access_log, 'r')
target_file = open(output_log, 'w')

# Find frequency
def find(list):
  # working dictionary to push into
  dic = {}
  for line in list:
    # look for a specific method
    match = re.search(method, line)
    if match:
      line = re.sub('^.*"' + method + '\s', '', line)
      # ignore css, js, png, jpg, gif, ico files
      # and /js/admin_menu/cache
      # and /batch
      useless = re.search(
          '\.(css|png|gif|jpg|js|ico|txt)|/js/admin_menu/cache|/batch',
          line)
      if not useless:
        line = re.sub('\s.*$', '', line)
        if line in dic.keys():
          dic[line] += 1
        else:
          dic[line] = 1
  return dic

# Sort dictionary by value
def sort_dic(dic):
  temp = [(v, k) for k, v in dic.items()]
  temp.sort()
  temp.reverse()
  temp = [(k, v) for v, k in temp]
  return temp

# Write file
def write_to_file(list):
  try:
    rep = sys.argv[4]
    print 'Repetition flag is set. Writing occurrence number.'
  except:
    rep = False
    print 'Repetition flag is not set.'
  for line in list:
    # if repetition is set, write additional info
    if rep:
      occur = str(line[1]) + '    ' + line[0] + '\n' 
    # otherwise write only URL
    else:
      occur = line[0] + '\n'
    target_file.write(occur)
  target_file.close()

# Script itself
if __name__ == '__main__':
  print 'Started parsing %s...' % access_log
  # read access.log
  list = original_file.readlines()
  dic = find(list)
  list = sort_dic(dic)
  write_to_file(list)
  total = len(dic)
  print 'Done! Wrote %s lines for %s method from %s to %s.' % (total,
                                                               method,
                                                               access_log,
                                                               output_log)
