#!/usr/bin/python3

### plan ###
# construct a list of "rock" coordinates from the input
# determine the Y coordinate where the "void" starts
# "pour sand" until one grain goes to the void
# 
#

from pprint import pprint
#import sys
import json

sand_entry_coord = [500, 0]
rock_coords = []

# read input
with open('day_14_input.txt') as f:
  input_rows = f.read().split("\n")

# parse input
# and store rock coordinates
for input_row in input_rows:
  input_row = '[[' + input_row + ']]'
  input_row = input_row.replace(' -> ','], [')
  input_row_orig_list = json.loads(input_row)
  for idx, item in enumerate(input_row_orig_list):
    if idx +1 == len(input_row_orig_list):
      break
    x1 = input_row_orig_list[idx][0]
    y1 = input_row_orig_list[idx][1]
    x2 = input_row_orig_list[idx + 1][0]
    y2 = input_row_orig_list[idx + 1][1]
    if x1 == x2:
      # keep incrementing y coordinate
      maxv = max(y1, y2)
      minv = min(y1, y2)
      for i in range(minv, maxv + 1):
        new_coord = [x1, i]
        if new_coord not in rock_coords:
          rock_coords.append(new_coord)
    elif y1 == y2:
      # keep incrementing x coordinate
      maxv = max(x1, x2)
      minv = min(x1, x2)
      for i in range(minv, maxv + 1):
        new_coord = [i, y1]
        if new_coord not in rock_coords:
          rock_coords.append(new_coord)
    else:
      print("You shouldn't be here...")

void_y_coord = max([c[1] for c in rock_coords]) + 1
rock_grains_count = len(rock_coords)
sand_grains_count = 0
tmp_coord = [0, 0]
#print(rock_coords)
#print(void_y_coord)

# pour that sand
while True:
  if tmp_coord[1] >= void_y_coord:
    break
  tmp_coord = sand_entry_coord.copy()
  while True:
    if tmp_coord[1] >= void_y_coord:
      break

    tmp_coord_under = [tmp_coord[0], tmp_coord[1] + 1]
    tmp_coord_under_left = [tmp_coord[0] - 1, tmp_coord[1] + 1]
    tmp_coord_under_right = [tmp_coord[0] + 1,tmp_coord[1] + 1]
  
    if tmp_coord_under not in rock_coords:
      tmp_coord = tmp_coord_under.copy()
    elif tmp_coord_under_left not in rock_coords:
      tmp_coord = tmp_coord_under_left.copy()
    elif tmp_coord_under_right not in rock_coords:
      tmp_coord = tmp_coord_under_right.copy()
    else:
      # sand grain will rest here
      rock_coords.append(tmp_coord)
      sand_grains_count+=1
      break

print(str(sand_grains_count) + " units of sand come to rest before sand starts flowing into the abyss.")
