#!/usr/bin/python3

my_dicts = {}

# populate dicts in my_dict with input data
with open('day_08_input.txt') as f:
  input_rows = f.read().split("\n")
  for y, my_row in enumerate(input_rows):
    for x, my_char in enumerate(my_row):
      my_dict = str(y) + "_" + str(x)
      my_dicts[my_dict] = {}
      my_dicts[my_dict]["y"] = y
      my_dicts[my_dict]["x"] = x
      my_dicts[my_dict]["visible_from_left"] = True # visible by default 
      my_dicts[my_dict]["visible_from_right"] = True
      my_dicts[my_dict]["visible_from_top"] = True
      my_dicts[my_dict]["visible_from_bottom"] = True
      my_dicts[my_dict]["visible"] = True # to be calculated later
      my_height = int(my_char)
      my_dicts[my_dict]["height"] = my_height

# for each item in my_dict, look at visibility from each direction by iterating through nested dictionary items
  for my_dict in my_dicts:
    x = my_dicts[my_dict]["x"]
    y = my_dicts[my_dict]["y"]
    height = my_dicts[my_dict]["height"]
    # check_visible_from_left
    # count "trees" at least he same hight
    if len([ d for d in my_dicts.values() if d['y'] == y if d['x'] < x if d['height'] >= height ]) > 0:
      my_dicts[my_dict]["visible_from_left"] = False
    # check_visible_from_right
    if len([ d for d in my_dicts.values() if d['y'] == y if d['x'] > x if d['height'] >= height ]) > 0:
      my_dicts[my_dict]["visible_from_right"] = False
    # check_visible_from_top
    if len([ d for d in my_dicts.values() if d['x'] == x if d['y'] < y if d['height'] >= height ]) > 0:
      my_dicts[my_dict]["visible_from_top"] = False
    # check_visible_from_bottom
    if len([ d for d in my_dicts.values() if d['x'] == x if d['y'] > y if d['height'] >= height ]) > 0:
      my_dicts[my_dict]["visible_from_bottom"] = False
    my_dicts[my_dict]["visible"] = my_dicts[my_dict]["visible_from_left"] or \
      my_dicts[my_dict]["visible_from_right"] or \
      my_dicts[my_dict]["visible_from_top"] or \
      my_dicts[my_dict]["visible_from_bottom"] 
  visible_count = len([ d for d in my_dicts.values() if d['visible'] == True ])
  print("Number of trees visible from outside the grid is " + str(visible_count))

    
    