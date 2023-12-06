#!/usr/bin/python3

lower_abc_str = "abcdefghijklmnopqrstuvwxyz"
upper_abc_str = lower_abc_str.upper()
full_abc = lower_abc_str + upper_abc_str

with open('day_03_input.txt') as f:
  array = f.read().split("\n")
  print(array)
  for idx, element in enumerate(array):
    # split array elements/strings into half
    half1 = element[:len(element)//2]
    half2 = element[len(element)//2:]
    # find common letter
    common_letter = set(half1).intersection(half2)
    common_letter_str = list(common_letter)[0]
    # now we have the common letters a string
    # let's find its "priority" value
    priority = full_abc.find(common_letter_str) + 1 # add 1 as indexing starts from 0
    # and store it into the array element
    array[idx] = priority
  print(array)
  print("Sum of all priorities for items in both rucksack compartments is " + str(sum(array)))

"""
plan:
for each row in the input, create 2 lists and find their intersection
--> that's the common letter in both "rucksack compartments"
then for each common letter, map it to a "priority"
finally, sum the priorties per input row 
"""