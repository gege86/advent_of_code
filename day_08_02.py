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
      my_dicts[my_dict]["trees_visible_left"] = 0 # to be calculated later 
      my_dicts[my_dict]["trees_visible_right"] = 0
      my_dicts[my_dict]["trees_visible_top"] = 0
      my_dicts[my_dict]["trees_visible_bottom"] = 0
      my_dicts[my_dict]["scenic_score"] = 0 # to be calculated later
      my_dicts[my_dict]["height"] = int(my_char)
# for each item in my_dict, check how many trees are visible in each direction
# by iterating through nested dictionary items
  for my_dict in my_dicts:
    x = my_dicts[my_dict]["x"]
    y = my_dicts[my_dict]["y"]
    my_height = my_dicts[my_dict]["height"]
    # check_visible_tree_count_left
    tree_heights_to_the_left = list([ d['height'] for d in my_dicts.values() if d['y'] == y if d['x'] < x ])
    tree_heights_to_the_left.reverse()
    trees_visible_left=0
    for tree_height in tree_heights_to_the_left:
      if tree_height >= my_height:
        trees_visible_left+=1
        break
      else:
        trees_visible_left+=1
    my_dicts[my_dict]["trees_visible_left"] = trees_visible_left
    # check_visible_tree_count_right
    tree_heights_to_the_right = list([ d['height'] for d in my_dicts.values() if d['y'] == y if d['x'] > x ])
    trees_visible_right=0
    for tree_height in tree_heights_to_the_right:
      if tree_height >= my_height:
        trees_visible_right+=1
        break
      else:
        trees_visible_right+=1
    my_dicts[my_dict]["trees_visible_right"] = trees_visible_right
    # check_visible_tree_count_top
    tree_heights_to_the_top = list([ d['height'] for d in my_dicts.values() if d['x'] == x if d['y'] < y ])
    tree_heights_to_the_top.reverse()
    trees_visible_top=0
    for tree_height in tree_heights_to_the_top:
      if tree_height >= my_height:
        trees_visible_top+=1
        break
      else:
        trees_visible_top+=1
    my_dicts[my_dict]["trees_visible_top"] = trees_visible_top
    # check_visible_tree_count_bottom
    tree_heights_to_the_bottom = list([ d['height'] for d in my_dicts.values() if d['x'] == x if d['y'] > y ])
    trees_visible_bottom=0
    for tree_height in tree_heights_to_the_bottom:
      if tree_height >= my_height:
        trees_visible_bottom+=1
        break
      else:
        trees_visible_bottom+=1
    my_dicts[my_dict]["trees_visible_bottom"] = trees_visible_bottom

    # calculate scenic score for tree
    my_dicts[my_dict]["scenic_score"] = my_dicts[my_dict]["trees_visible_left"] * \
      my_dicts[my_dict]["trees_visible_right"] * \
      my_dicts[my_dict]["trees_visible_top"] * \
      my_dicts[my_dict]["trees_visible_bottom"]
  
  # solution
  scenic_scores_list = list([ d['scenic_score'] for d in my_dicts.values() ])
  print(scenic_scores_list)
  print("Highest scenic score possible for any tree is " + str(max(scenic_scores_list)))
    
    