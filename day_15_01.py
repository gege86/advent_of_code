#!/usr/bin/python3

### plan ###
# store sensor positions and their distance to the closest beacon
# print it out
# no clue what next
# 
#

from pprint import pprint
from math import sqrt

# https://www.statology.org/manhattan-distance-python/
def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

where_beacon_cant_be = set()
beacon_set = set()
sensor_set = set()
input_lst = []


# read input
with open('day_15_input.txt') as f:
  input_rows = f.read().split("\n")

# parse input
for input_row in input_rows:
  # sensor x,y
  x = int(input_row.split()[2].split('=')[1].split(',')[0])
  y = int(input_row.split()[3].split('=')[1].split(':')[0])
  # beacon x,y
  bx = int(input_row.split()[8].split('=')[1].split(',')[0])
  by = int(input_row.split()[9].split('=')[1])
  # manhattan distance
  m = manhattan((x,y),(bx,by))
  my_tuple = (x,y,bx,by,m)
  input_lst.append(my_tuple)
  beacon_set.add((bx,by))
  sensor_set.add((x,y))

print("input is parsed")

for sensor in input_lst:
  x = sensor[0]
  y = sensor[1]
  m = sensor[4]
  from_x = x - m if x - m >= 0 else 0
  to_x = x + m + 1 if x + m + 1 <= 4000000 else 4000000
  from_y = y - m if y - m >= 0 else 0
  to_y = y + m + 1 if y + m + 1 <= 4000000 else 4000000
  print("Processing a sensor.")
  for i in range(x - m, x + m + 1):
    for j in range(y - m, y + m + 1):
    j = 2000000
      if m >= manhattan((x,y),(i,j)):
        if (i,j) not in beacon_set and (i,j) not in sensor_set:
          where_beacon_cant_be.add((i,j))
  #          print(len(where_beacon_cant_be))

print("know we know where a beacon can't be")

#print(where_beacon_cant_be)
y_10_count = 0
coords_tmp = []
for coord in where_beacon_cant_be:
  if coord[1] == 2000000:
    y_10_count+=1
print(y_10_count)

