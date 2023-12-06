#!/usr/bin/python3

my_dicts = {}

def count_visible_trees(tree_heights_list, my_height):
  trees_visible=0
  for tree_height in tree_heights_list:
    if tree_height >= my_height:
      trees_visible+=1
      break
    else:
      trees_visible+=1
  return trees_visible

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
    my_dicts[my_dict]["trees_visible_left"] = count_visible_trees(tree_heights_to_the_left, my_height)
    # check_visible_tree_count_right
    tree_heights_to_the_right = list([ d['height'] for d in my_dicts.values() if d['y'] == y if d['x'] > x ])
    my_dicts[my_dict]["trees_visible_right"] = count_visible_trees(tree_heights_to_the_right, my_height)
    # check_visible_tree_count_top
    tree_heights_to_the_top = list([ d['height'] for d in my_dicts.values() if d['x'] == x if d['y'] < y ])
    tree_heights_to_the_top.reverse()
    my_dicts[my_dict]["trees_visible_top"] = count_visible_trees(tree_heights_to_the_top, my_height)
    # check_visible_tree_count_bottom
    tree_heights_to_the_bottom = list([ d['height'] for d in my_dicts.values() if d['x'] == x if d['y'] > y ])
    my_dicts[my_dict]["trees_visible_bottom"] = count_visible_trees(tree_heights_to_the_bottom, my_height)

    # calculate scenic score for tree
    my_dicts[my_dict]["scenic_score"] = my_dicts[my_dict]["trees_visible_left"] * \
      my_dicts[my_dict]["trees_visible_right"] * \
      my_dicts[my_dict]["trees_visible_top"] * \
      my_dicts[my_dict]["trees_visible_bottom"]
  
  # solution
  scenic_scores_list = list([ d['scenic_score'] for d in my_dicts.values() ])
  #print(scenic_scores_list)
  print("Highest scenic score possible for any tree is " + str(max(scenic_scores_list)))
    
    