#!/usr/bin/python3

### plan ###
# iterate through the input 
# store each cycle number and the value during it based on the instructions in the input
# finally: for cycles 20, 60, 100, 140, 180, 220 take the product of the cycle number and the value and sum these 5 values.
# 
# to check if pixel is to be drawn:
#   mod 40 the cpu cycle, subtract 1
#   compare that value to X, X-1, X+1
#   if it matches any of those, draw the pixel
#   store that value as boolean in the list

current_cpu_cycle = 0
X = 1 # register for CPU value
cycles_values_list = [] # store cycles and with it, value during cycle execution

def check_if_pixel_draw():
  cursor_x_horizontal_position = (current_cpu_cycle % 40) - 1
  if cursor_x_horizontal_position == -1: # handle literal edge case...
    cursor_x_horizontal_position = 39
  if cursor_x_horizontal_position in [X, X - 1, X + 1]:
    draw_pixel = True
  else:
    draw_pixel = False
  return draw_pixel

with open('day_10_input.txt') as f:
  input_rows = f.read().split("\n")
  for my_row in input_rows:
    if my_row == "noop":
      current_cpu_cycle+=1
      cycles_values_list.append([current_cpu_cycle, X, check_if_pixel_draw()])
      current_sprite_position = X
    elif my_row.split()[0] == "addx":
      current_cpu_cycle+=1
      cycles_values_list.append([current_cpu_cycle, X, check_if_pixel_draw()])
      current_cpu_cycle+=1
      cycles_values_list.append([current_cpu_cycle, X, check_if_pixel_draw()])
      X = X + int(my_row.split()[1])

# "draw picture"
print(cycles_values_list)
for x in range(0, 6):
  print(" ")
  for i in range(0, 40):
    if cycles_values_list[x*40 + i][2]:
      my_str = '#'
    else:
      my_str = '.'
    print(my_str, end ="")
    

