#!/usr/bin/python3

### plan ###
# think of a method to sort the list of lists until it's all sorted
# 
# 

from pprint import pprint
#import sys
import json

def is_right_order(left, right):
  if type(left) is int and type(right) is int:
    if left < right:
      return True
    elif left > right:
      return False
 
  if type(left) is list and type(right) is list:
    for i in range(0, min(len(left),len(right)) + 1):
      if i == min(len(left),len(right)):
        if len(left) > len(right):
          return False
        elif len(left) < len(right):
          return True
        elif len(left) == len(right):
          break
      else:
        if is_right_order(left[i], right[i]) != None:
          return is_right_order(left[i], right[i])

  if type(left) is int and type(right) is list:
    return is_right_order([left], right)

  if type(left) is list and type(right) is int:
    return is_right_order(left, [right])
 
# read input
# and add extra 2 items
with open('day_13_input.txt') as f:
  lines = (line.rstrip() for line in f) 
  lines = list(json.loads(line) for line in lines if line) # Non-blank lines in a list
  # thanks
  # https://stackoverflow.com/questions/4842057/easiest-way-to-ignore-blank-lines-when-reading-a-file-in-python
  lines.append([[2]])
  lines.append([[6]])

while True:
  all_in_right_order = True
  for idx, item in enumerate(lines):
    if idx + 1 == len(lines):
      break
    left_list = lines[idx]
    right_list = lines[idx + 1]
    if is_right_order(left_list, right_list) == False:
      lines[idx], lines[idx + 1] = lines[idx + 1], lines[idx]
      all_in_right_order = False
  if all_in_right_order == True:
    break
#pprint(lines)
# YES!!!!

position1 = lines.index([[2]]) + 1
position2 = lines.index([[6]]) + 1
decoder_key = position1 * position2
print("The decoder key for the distress signal is " + (str(decoder_key)) + ".")
