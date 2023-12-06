#!/usr/bin/python3


with open('day_06_input.txt') as f:
  input_rows = f.read().split("\n")
  for input_row in input_rows:
    for i, c in enumerate(input_row):
      # list of 4 subsequent chars
      four_char_list = [input_row[i], input_row[i+1], input_row[i+2], input_row[i+3]]
     
      # check if chars are unique
      if len(four_char_list) == len(set(four_char_list)):
        print("First four unique chars are " + str(four_char_list))
        print("First marker after char " + str(i+4)) # add 4 instead of 3 to offset counting array from 0
        break
