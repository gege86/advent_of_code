#!/usr/bin/python3


with open('day_06_input.txt') as f:
  input_rows = f.read().split("\n")
  for input_row in input_rows:
    for i, c in enumerate(input_row):
      # list of 14 subsequent chars
      fourteen_char_list = [input_row[i],
                            input_row[i+1],
                            input_row[i+2],
                            input_row[i+3],
                            input_row[i+4],
                            input_row[i+5],
                            input_row[i+6],
                            input_row[i+7],
                            input_row[i+8],
                            input_row[i+9],
                            input_row[i+10],
                            input_row[i+11],
                            input_row[i+12],
                            input_row[i+13]]
     
      # check if chars are unique
      if len(fourteen_char_list) == len(set(fourteen_char_list)):
        print("First four unique chars are " + str(fourteen_char_list))
        print("First marker after char " + str(i+14)) # add 14 instead of 13 to offset counting array from 0
        break
