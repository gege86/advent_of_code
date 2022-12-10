#!/usr/bin/python3

### plan ###
# iterate through the input 
# store each cycle number and the value during it based on the instructions in the input
# finally: for cycles 20, 60, 100, 140, 180, 220 take the product of the cycle number and the value and sum these 5 values.
# 
# 
#

current_cpu_cycle = 0
X = 1 # register for CPU value
cycles_values_list = [] # store cycles and with it, value during cycle execution

with open('day_10_input.txt') as f:
  input_rows = f.read().split("\n")
  for my_row in input_rows:
    if my_row == "noop":
      current_cpu_cycle+=1
      cycles_values_list.append([current_cpu_cycle, X])
    elif my_row.split()[0] == "addx":
      current_cpu_cycle+=1
      cycles_values_list.append([current_cpu_cycle, X])
      current_cpu_cycle+=1
      cycles_values_list.append([current_cpu_cycle, X])
      X = X + int(my_row.split()[1])

# ok this is a bit ugly, because:
# the list index we are referring to is one smaller than the CPU cycle number
product1 = cycles_values_list[19][0] * cycles_values_list[19][1]
product2 = cycles_values_list[59][0] * cycles_values_list[59][1]
product3 = cycles_values_list[99][0] * cycles_values_list[99][1]
product4 = cycles_values_list[139][0] * cycles_values_list[139][1]
product5 = cycles_values_list[179][0] * cycles_values_list[179][1]
product6 = cycles_values_list[219][0] * cycles_values_list[219][1]

print(cycles_values_list)

sum_product = product1 + product2 + product3 + product4 + product5 + product6
print("The sum of signal strengths during the 20th, 60th, 100th, 140th, 180th, and 220th cycles is " + str(sum_product) + ".")