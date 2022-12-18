#!/usr/bin/python3

### plan ###
# store sensor positions and their distance to the closest beacon
# create a set with all possible distress signal positions
# remove from that set everything we can
# at the end there should only be one possible location


# https://www.statology.org/manhattan-distance-python/
def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

distress_possible_locations = set()
beacon_set = set()
sensor_set = set()
input_lst = []
tmp_list = []

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

print("Input is parsed")

# fill set of possible distress signal locations
maxv = 4000000
for i in range(0, maxv + 1):
  for j in range(0, maxv + 1):
    distress_possible_locations.add((i, j))
print("Possible distress signal locations stored.")

# remove locations where we know that the distress signal can't be
for sensor in input_lst:
  x = sensor[0]
  y = sensor[1]
  m = sensor[4]
  print("Processing a sensor.")
  for i in range(0, m + 1):
    distress_possible_locations.discard((x + i, y + i))
    distress_possible_locations.discard((x + i, y - i))
    distress_possible_locations.discard((x - i, y + i))
    distress_possible_locations.discard((x - i, y - i))

print("Now only one possible distress signal location should remain.")
print(distress_possible_locations)
