#!/usr/bin/python3

### plan ###
# think up a data structure to store a "monkey" and its attributes
# iterate through that for the win
# 
# 
"""
[
    {
        "items" : [79, 98],
        "operation_part_1" : "old",
        "operation_part_2" : "*",
        "operation_part_3" : "19",
        "divisible_by" : 23,
        "monkey_num_if_true" : 2,
        "monkey_num_if_false" : 3,
        "inspected_count" : 0
    },
    # ... etc. other monkeys...
]
"""
from pprint import pprint
monkey_list = []
monkey_dict_tmp = {}

# read input
with open('day_11_input.txt') as f:
  input_blocks = f.read().split("\n\n")
  for block in input_blocks:
    monkey_num = int(block.split("\n")[0].split()[1][0])
    items = [ int(i) for i in block.split("\n")[1].split(':')[1].split(',') ]
    operation_part_1 = block.split("\n")[2].split()[3]
    operation_part_2 = block.split("\n")[2].split()[4]
    operation_part_3 = block.split("\n")[2].split()[5]
    divisible_by = int(block.split("\n")[3].split()[3])
    monkey_num_if_true = int(block.split("\n")[4].split()[5])
    monkey_num_if_false = int(block.split("\n")[5].split()[5])
    monkey_dict_tmp = {
      "items" : items,
      "operation_part_1" : operation_part_1,
      "operation_part_2" : operation_part_2,
      "operation_part_3" : operation_part_3,
      "divisible_by" : divisible_by,
      "monkey_num_if_true" : monkey_num_if_true,
      "monkey_num_if_false" : monkey_num_if_false,
      "inspected_count" : 0
    }
    monkey_list.append(monkey_dict_tmp)

# let's define this separately
def operation():
  if monkey_list[m]['operation_part_1'] == "old":
    op1 = item
  if monkey_list[m]['operation_part_3'] == "old":
    op3 = item
  else:
    op3 = int(monkey_list[m]['operation_part_3'])
  if monkey_list[m]['operation_part_2'] == "+":
    result = op1 + op3
  elif monkey_list[m]['operation_part_2'] == "*":
    result = op1 * op3

  result = result // 3
  return result


# now play X rounds
X = 20
for round in range(0, X):
  for m in range(len(monkey_list)):
    for idx, item in enumerate(monkey_list[m]['items']):
      item = operation()
      monkey_list[m]['inspected_count']+=1
      monkey_list[m]['items'][idx] = item
    tmp_items = monkey_list[m]['items'].copy()
    for item in tmp_items:
      if item % monkey_list[m]['divisible_by'] == 0:
        to_monkey = monkey_list[m]['monkey_num_if_true']
      else:
        to_monkey = monkey_list[m]['monkey_num_if_false']
      monkey_list[to_monkey]['items'].append(monkey_list[m]['items'].pop(0))
#pprint(monkey_list)
inspection_count_list = sorted([ i['inspected_count'] for i in monkey_list ])
print("Inspection counts per monkey: " + str(inspection_count_list))
largest_i_count_01 = inspection_count_list.pop()
largest_i_count_02 = inspection_count_list.pop()
monkey_business_value = largest_i_count_01 * largest_i_count_02
print("Monkey business value after " + str(X) + " rounds is: " + str(monkey_business_value) + ".")