#!/usr/bin/python3

### plan ###
# write a function that can compare stuff : D
# 
# 

#from pprint import pprint
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
 
#print(is_right_order([5,5],[5,6]))

# read input
with open('day_13_input.txt') as f:
  input_blocks = f.read().split("\n\n")
  counter = 0
  sum_indeces = 0
  for block in input_blocks:
    counter+=1
    left_list = json.loads(block.split("\n")[0])
    right_list = json.loads(block.split("\n")[1])
    #print(left_list)
    #print(right_list)
    #print(is_right_order(left_list, right_list))
    check = is_right_order(left_list, right_list)
    if check == True:
      sum_indeces = sum_indeces + counter

print("The sum of indices for the pairs that are in the right order is: " + str(sum_indeces) + ".")