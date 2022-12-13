#!/usr/bin/python3

### plan ###
# think up a data structure to store a "monkey" and its attributes
# iterate through that for the win
# 
### plan for task 02 ###
# this is getting really slow
# "worry" values for items are indeed have ridiculous values after a few hundred rounds : )
# python3 -m trace --trace day_11_02.py
# shows that the slow operations are integer multiplications
# so I googled how to make it faster
# one way is to use a non-default library for some math calculations (like multiplication)
# so let's try that (gmpy2 module)
# ok this is faster, but still a slog... slows down to pretty much a halt before reaching round 400
# 
# idea2: there can be "closed loops" between monkeys if an item is divisable by multiple monkeys' "test" numbers
# what I'll try to do is not do the integer multiplication if I find such loops, just move the package to another monkey
# utltimately we don't care about the "worry level" of the package
# idea3: well that didn't quite work. There is no loop with just 2 monkeys. So my plan is to follow one package's route
# and try to find some loops
# sub-idea: the monkey that square the worry value is the worst. Try to isolate that. Where does the package go from it?
# 
# "solution":
# I found repeating patterns but finding them and handling them is really ugly...
# still: must.get.stars...

import gmpy2
from gmpy2 import mpz
from pprint import pprint
import sys
monkey_list = []
monkey_dict_tmp = {}
item_from_pack_name_idx = 0
w = {} # to store recurring worry_values
r = [] # to store helper values for recurring worry_values

# read input
with open('day_11_input.txt') as f:
  input_blocks = f.read().split("\n\n")
  for block in input_blocks:
    monkey_num = int(block.split("\n")[0].split()[1][0])
    items = [ int(i) for i in block.split("\n")[1].split(':')[1].split(',') ]
    for idx, my_item in enumerate(items):
      items[idx] = {
        "name" : item_from_pack_name_idx,
        "worry_value" : my_item
      }
      item_from_pack_name_idx+=1
      
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
#pprint(monkey_list)


# let's define this separately
def operation():
  if monkey_list[m]['operation_part_1'] == "old":
    op1 = item['worry_value']
  if monkey_list[m]['operation_part_3'] == "old":
    op3 = item['worry_value']
  else:
    op3 = int(monkey_list[m]['operation_part_3'])
  if monkey_list[m]['operation_part_2'] == "+":
    result = op1 + op3
  elif monkey_list[m]['operation_part_2'] == "*":
    #result = op1 * op3
    result = mpz(mpz(op1) * mpz(op3))

  #result = result // 3
  return result

lol = int(sys.argv[1])
print(type(lol))
round_track_01 = 0
# now play X rounds
X = 400
for round in range(0, X):
#  if round > 294:
#    print(round)
  #monkeyz = [[ i['name'] for i in d['items'] if i['name'] == 0 ] for d in monkey_list ]
  #if round > 40:
  #  pprint(monkeyz)
  for m in range(len(monkey_list)):
    for idx, item in enumerate(monkey_list[m]['items']):
      item['worry_value'] = operation()
      monkey_list[m]['inspected_count']+=1
      monkey_list[m]['items'][idx] = item
    tmp_items = monkey_list[m]['items'].copy()
    for item in tmp_items:
      if item['worry_value'] % monkey_list[m]['divisible_by'] == 0:
        to_monkey = monkey_list[m]['monkey_num_if_true']
      else:
        to_monkey = monkey_list[m]['monkey_num_if_false']
      monkey_list[to_monkey]['items'].append(monkey_list[m]['items'].pop(0))
# I'm fishing for repeating patterns here...
    
#    if m == 2 and monkey_list[to_monkey]['items'][-1]['name'] == 3:
#      diff = round - round_track_01
#      round_track_01 = round
#      print(str(diff) + " " + str(round) + " Packet " + str(monkey_list[to_monkey]['items'][-1]['name']) + " went from monkey 2 to number " + str(to_monkey))
      
      #if to_monkey == 2 and monkey_list[to_monkey]['items'][-1]['name'] == int(sys.argv[1]):
      if monkey_list[to_monkey]['items'][-1]['name'] == int(sys.argv[1]):
        diff = round - round_track_01
        round_track_01 = round
        print(str(diff) + " " + str(round) + " Packet " + str(monkey_list[to_monkey]['items'][-1]['name']) + " went from monkey " + str(m) + " to number " + str(to_monkey))

      r = [[0,57,16],
           [1,31,16],
           [2,0,0],
           [3,0,0],
           [4,40,16],
           [5,0,0],
           [6,0,0],
           [7,22,16],
           [8,20,16],
           [9,29,16],
           [10,0,0],
           [11,0,0],
           [12,17,16],
           [13,0,0],
           [14,0,0],
           [15,0,0],
           [16,0,0],
           [17,36,16],
           [18,0,0],
           [19,0,0],
           [20,42,16],
           [21,0,0],
           [22,0,0],
           [23,0,0],
           [24,0,0],
           [25,17,16],
           [26,0,0],
           [27,0,0],
           [28,0,0],
           [29,0,0],
           [30,0,0],
           [31,0,0],
           [32,0,0],
           [33,22,16],
           [34,0,0],
           [35,0,0]]
#      my_name = 0
#      my_round = 57
#      my_diff = 16
#      if to_monkey == 2 and monkey_list[to_monkey]['items'][-1]['name'] == my_name and round == my_round:
#        w[my_name] = [ x for x in monkey_list[to_monkey]['items'] if x['name'] == my_name ][0]['worry_value']
#      if (round - my_round) % my_diff == 0 and round > my_round and to_monkey == 2 and monkey_list[to_monkey]['items'][-1]['name'] == my_name and round == my_round:
#        [ x for x in monkey_list[to_monkey]['items'] if x['name'] == my_name ][0]['worry_value'] = w[my_name]
      for items in r:
        my_name = items[0]
        my_round = items[1]
        my_diff = items[2]
        if my_diff == 0:
          continue
        if to_monkey == 2 and monkey_list[to_monkey]['items'][-1]['name'] == my_name and round == my_round:
          w[my_name] = [ x for x in monkey_list[to_monkey]['items'] if x['name'] == my_name ][0]['worry_value']
        if (round - my_round) % my_diff == 0 and round > my_round and to_monkey == 2 and monkey_list[to_monkey]['items'][-1]['name'] == my_name and round == my_round:
          [ x for x in monkey_list[to_monkey]['items'] if x['name'] == my_name ][0]['worry_value'] = w[my_name]

        #print(str(round) + " Packet " + str(monkey_list[to_monkey]['items'][-1]['name']) + " went from monkey 2 to number " + str(to_monkey))
  
#    if m == 2 and to_monkey == 3 and monkey_list[to_monkey]['items'][-1]['name'] == 0:
#      print(str(round) + " Packet " + str(monkey_list[to_monkey]['items'][-1]['name']) + " went from monkey 2 to number " + str(to_monkey))
#    if m == 2 and to_monkey == 3 and monkey_list[to_monkey]['items'][-1]['name'] == 4:
#      print(str(round) + " Packet " + str(monkey_list[to_monkey]['items'][-1]['name']) + " went from monkey 2 to number " + str(to_monkey))
#    if m == 2 and to_monkey == 3 and monkey_list[to_monkey]['items'][-1]['name'] == 9:
#      print(str(round) + " Packet " + str(monkey_list[to_monkey]['items'][-1]['name']) + " went from monkey 2 to number " + str(to_monkey))

#      if round == 479 and m == 2 and to_monkey == 3 and monkey_list[to_monkey]['items'][-1]['name'] == 0:
#        w0 = [ x for x in monkey_list[3]['items'] if x['name'] == 0 ][0]['worry_value']
#      if (round - 479) % 171 == 0 and round > 479 and m == 2 and to_monkey == 3 and monkey_list[to_monkey]['items'][-1]['name'] == 0:
#        [ x for x in monkey_list[3]['items'] if x['name'] == 0 ][0]['worry_value'] = w0
#      if round == 419 and m == 2 and to_monkey == 3 and monkey_list[to_monkey]['items'][-1]['name'] == 4:
#        w4 = [ x for x in monkey_list[3]['items'] if x['name'] == 4 ][0]['worry_value']
#      if (round - 419) % 171 == 0 and round > 419 and m == 2 and to_monkey == 3 and monkey_list[to_monkey]['items'][-1]['name'] == 4:
#        [ x for x in monkey_list[3]['items'] if x['name'] == 4 ][0]['worry_value'] = w4
#      if round == 539 and m == 2 and to_monkey == 3 and monkey_list[to_monkey]['items'][-1]['name'] == 9:
#        w9 = [ x for x in monkey_list[3]['items'] if x['name'] == 9 ][0]['worry_value']
#      if (round - 539) % 171 == 0 and round > 539 and m == 2 and to_monkey == 3 and monkey_list[to_monkey]['items'][-1]['name'] == 9:
#        [ x for x in monkey_list[3]['items'] if x['name'] == 9 ][0]['worry_value'] = w9
  # i need a rule for w9 also

 # if round == 131:
 #   w8 = [ x for x in monkey_list[1]['items'] if x['name'] == 8 ][0]['worry_value']
 # if round == 201:
 #   w1 = [ x for x in monkey_list[1]['items'] if x['name'] == 1 ][0]['worry_value']
 # if round == 231:
 #   w7 = [ x for x in monkey_list[1]['items'] if x['name'] == 7 ][0]['worry_value']
 # if round == 254:
 #   w3 = [ x for x in monkey_list[1]['items'] if x['name'] == 3 ][0]['worry_value']
 # if round == 277:
 #   w2 = [ x for x in monkey_list[1]['items'] if x['name'] == 2 ][0]['worry_value']
 # if round == 389:
 #   w5 = [ x for x in monkey_list[1]['items'] if x['name'] == 5 ][0]['worry_value']
 # if round == 406:
 #   w6 = [ x for x in monkey_list[1]['items'] if x['name'] == 6 ][0]['worry_value']
  

#  if (round - 131) % 448 == 0:
#    [ x for x in monkey_list[1]['items'] if x['name'] == 8 ][0]['worry_value'] = w8
#  if (round - 201) % 448 == 0:
#    [ x for x in monkey_list[1]['items'] if x['name'] == 1 ][0]['worry_value'] = w1
#  if (round - 231) % 448 == 0:
#    [ x for x in monkey_list[1]['items'] if x['name'] == 7 ][0]['worry_value'] = w7
#  if (round - 254) % 448 == 0:
#    [ x for x in monkey_list[1]['items'] if x['name'] == 3 ][0]['worry_value'] = w3
#  if (round - 277) % 448 == 0:
#    [ x for x in monkey_list[1]['items'] if x['name'] == 2 ][0]['worry_value'] = w2
#  if (round - 389) % 448 == 0:
#    [ x for x in monkey_list[1]['items'] if x['name'] == 5 ][0]['worry_value'] = w5
#  if (round - 406) % 448 == 0:
#    [ x for x in monkey_list[1]['items'] if x['name'] == 6 ][0]['worry_value'] = w6
    

    #scenic_scores_list = list([ d['scenic_score'] for d in my_dicts.values() ])
    #monkeyz = [[ i['name'] for i in d['items']] for d in monkey_list ]
    #pprint(monkeyz)
      #pprint([ v['items']['worry_value'] for v in monkeyz])
      #if monkey_list[to_monkey]['items'][-1]['name'] == 0:
        #print(monkey_list[to_monkey]['items'][-1]['name'])
"""
1 7 3 2 5 6 8
[[7, 2, 6, 5], [8, 1, 4, 9, 3, 0], [], []]
[[7, 2, 6, 0, 5], [8, 9, 1, 4, 3], [], []]
[[0, 7, 4, 9, 2, 6, 5], [8, 1, 3], [], []]

"""
#pprint(monkey_list)
inspection_count_list = sorted([ i['inspected_count'] for i in monkey_list ])
print("Inspection counts per monkey: " + str(inspection_count_list))
largest_i_count_01 = inspection_count_list.pop()
largest_i_count_02 = inspection_count_list.pop()
monkey_business_value = largest_i_count_01 * largest_i_count_02
print("Monkey business value after " + str(X) + " rounds is: " + str(monkey_business_value) + ".")

for i in range(0, 4):
  print([x['name'] for x in monkey_list[i]['items']])
  print([len(x['worry_value']) for x in monkey_list[i]['items']])
  