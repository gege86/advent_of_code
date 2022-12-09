#!/usr/bin/python3

### plan ###
# create a list of lists for the 'head' movement. Nested list items: x, y coordinates. 
# create a list of lists for the 'tail' movement. Nested list items: x, y coordinates. 
# for the solution, count the lists in the 'tail' movement list
# will need a function for movement and loop it. The tail movement following the head has to be within the loop.
# 
#

list_of_visited_coordinates_head = [[0, 0]]
list_of_visited_coordinates_tail = [[0, 0]]
coordinates_head = [0, 0]
coordinates_tail = [0, 0]

def move_head(from_x, from_y, direction):
  if direction == "L":
    to_x = from_x - 1
    to_y = from_y
  if direction == "R":
    to_x = from_x + 1
    to_y = from_y
  if direction == "U":
    to_y = from_y + 1
    to_x = from_x
  if direction == "D":
    to_y = from_y - 1
    to_x = from_x
  
  return [to_x, to_y]

def move_tail(tail_x, tail_y, head_x, head_y):
  if head_x - tail_x > 1:
    to_x = head_x - 1
    to_y = head_y
  elif head_x - tail_x < -1:
    to_x = head_x + 1
    to_y = head_y
  elif head_y - tail_y > 1:
    to_x = head_x
    to_y = head_y - 1
  elif head_y - tail_y < -1:
    to_x = head_x
    to_y = head_y + 1
  else:
    to_x = tail_x
    to_y = tail_y
  
  return [to_x, to_y]

with open('day_09_input.txt') as f:
  input_rows = f.read().split("\n")
  for my_row in input_rows:
    step_direction = my_row.split()[0]
    step_count = int(my_row.split()[1])
    for i in range(0, step_count):
      coordinates_head = move_head(coordinates_head[0], coordinates_head[1], step_direction)
      coordinates_tail = move_tail(coordinates_tail[0], coordinates_tail[1], coordinates_head[0], coordinates_head[1])
      if coordinates_tail not in list_of_visited_coordinates_tail:
        list_of_visited_coordinates_tail.append(coordinates_tail)
  print("The tail of the rope visited " + str(len(list_of_visited_coordinates_tail)) + " positions at least once.")
