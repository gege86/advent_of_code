#!/usr/bin/python3

current_dirs = []
my_dict = {}

with open('day_07_input.txt') as f:
  input_rows = f.read().split("\n")
  for input_row in input_rows:
    if input_row[:4] == '$ cd':
      if input_row[:7] == '$ cd ..':
        current_dirs.pop()
        curr_dir_depth=len(current_dirs)
      else:
        current_dir = input_row[5:]
        current_dirs.append(current_dir)
        current_dir_str=str(current_dirs)
        my_dict[current_dir_str] = 0
    elif input_row[:4] == '$ ls':
      pass
    elif input_row[:4] == 'dir ':
      pass
    else:
      file_size = int(input_row.split()[0]) 
      file_name = input_row.split()[1] # we don't care
      # DO NOT store file size and file name as key value pair
      # DO add to sum_file_size for each directory list item somehow
      curr_dir_depth=len(current_dirs)
      tmp_current_dirs = current_dirs.copy()
      for level in range(curr_dir_depth):
        tmp_current_dir_str=str(tmp_current_dirs)
        my_dict[tmp_current_dir_str] += file_size
        tmp_current_dirs.pop()
  #print(my_dict)
  limit_x = 100000
  sum_dir_sizes_less_than_100k = sum([my_dict[i] for i in my_dict if my_dict[i] <= limit_x])
  print("Sum of directory sizes with less than 100k size is " + str(sum_dir_sizes_less_than_100k))
