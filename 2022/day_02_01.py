#!/usr/bin/python3

with open('day_02_input.txt') as f:
  array = f.read().split("\n")
  #print(array)
  """
  A rock X 1
  B paper Y 2
  C scissors Z 3
  
  win 6
  draw 3
  lose 0 
  
  # scores for each outcome:
  A X = 1 + 3 = 4
  A Y = 2 + 6 = 8
  A Z = 3 + 0 = 3
  B X = 1 + 0 = 1
  B Y = 2 + 3 = 5
  B Z = 3 + 6 = 9
  C X = 1 + 6 = 7
  C Y = 2 + 0 = 2
  C Z = 3 + 3 = 6
  """

  for idx, element in enumerate(array):
    if element == 'A X':
      array[idx] = 4
    if element == 'A Y':
      array[idx] = 8
    if element == 'A Z':
      array[idx] = 3
    if element == 'B X':
      array[idx] = 1
    if element == 'B Y':
      array[idx] = 5
    if element == 'B Z':
      array[idx] = 9
    if element == 'C X':
      array[idx] = 7
    if element == 'C Y':
      array[idx] = 2
    if element == 'C Z':
      array[idx] = 6
  print(array)
  print("Total score following the strategy guide is " + str(sum(array)))