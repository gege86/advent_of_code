#!/usr/bin/python3

sum_overlapping_pairs = 0

with open('day_04_input.txt') as f:
  list = f.read().split("\n")
  for element in list:
    # split string into two
    elf1 = element.split(",")[0]
    elf2 = element.split(",")[1]
    # split more to get "from" and "to" values per elf
    elf1_from = int(elf1.split("-")[0])
    elf1_to = int(elf1.split("-")[1])
    elf2_from = int(elf2.split("-")[0])
    elf2_to = int(elf2.split("-")[1])
    # now create lists, spanning "from" - "to"
    elf1_range = []
    i = elf1_from
    while i <= elf1_to:
      elf1_range.append(i)
      i += 1
    elf2_range = []
    i = elf2_from
    while i <= elf2_to:
      elf2_range.append(i)
      i += 1
    # now create sets
    elf1_range_set = set(elf1_range)
    elf2_range_set = set(elf2_range)
    # now check if one set overlaps the other
    if not elf1_range_set.isdisjoint(elf2_range_set):
      sum_overlapping_pairs += 1    

  print("Sum of overlapping elf assignment pairs is " + str(sum_overlapping_pairs) + ".")
