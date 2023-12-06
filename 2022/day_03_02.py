#!/usr/bin/python3

lower_abc_str = "abcdefghijklmnopqrstuvwxyz"
upper_abc_str = lower_abc_str.upper()
full_abc = lower_abc_str + upper_abc_str
prio_sum = 0

with open('day_03_input.txt') as f:
  array = f.read().split("\n")
  print(array)
  for idx, element in enumerate(array):
    # we only care about every third item - input file is 300 lines luckily
    if (idx + 1) % 3 == 0 :
      str1 = array[idx - 2]
      str2 = array[idx - 1]
      str3 = array[idx]
      # find common letter
      common_letter = set(str1).intersection(str2).intersection(str3)
      common_letter_str = list(common_letter)[0]
      # now we have the common letter as string
      # let's find its "priority" value
      priority = full_abc.find(common_letter_str) + 1 # add 1 as indexing starts from 0
      # and add it to the final sum
      prio_sum = prio_sum + priority
  print("Sum of all priorities for common items in elf groups is " + str(prio_sum))
