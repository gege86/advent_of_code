#!/usr/bin/python3

"""
            [L] [M]         [M]    
        [D] [R] [Z]         [C] [L]
        [C] [S] [T] [G]     [V] [M]
[R]     [L] [Q] [B] [B]     [D] [F]
[H] [B] [G] [D] [Q] [Z]     [T] [J]
[M] [J] [H] [M] [P] [S] [V] [L] [N]
[P] [C] [N] [T] [S] [F] [R] [G] [Q]
[Z] [P] [S] [F] [F] [T] [N] [P] [W]
 1   2   3   4   5   6   7   8   9 
"""

box_stacks = []
box_stacks.append("dirty_ofsetter_value_gege")
box_stacks.append(["Z","P","M","H","R"])
box_stacks.append(["P","C","J","B"])
box_stacks.append(["S","N","H","G","L","C","D"])
box_stacks.append(["F","T","M","D","Q","S","R","L"])
box_stacks.append(["F","S","P","Q","B","T","Z","M"])
box_stacks.append(["T","F","S","Z","B","G"])
box_stacks.append(["N","R","V"])
box_stacks.append(["P","G","L","T","D","V","C","M"])
box_stacks.append(["W","Q","N","J","F","M","L"])


with open('day_05_input.txt') as f:
  input_rows = f.read().split("\n")
  for input_row in input_rows:
    moves_count = int(input_row.split()[1])
    from_box_stack = int(input_row.split()[3])
    to_box_stack = int(input_row.split()[5])
    for i in range(0,moves_count):
      box_str = box_stacks[from_box_stack].pop()
      box_stacks[to_box_stack].append(box_str)
  
  answer_str = ""
  for i in range(0,9):
    box_str = box_stacks[i+1].pop()
    answer_str = answer_str + box_str
  print(answer_str)
