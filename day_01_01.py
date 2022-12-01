
# get the sum of calories for the elf carrying the most calories

# read stuff into 2 dimensional array(?) - thanks stackoverflow
with open('list.txt') as f:
  array = [[int(num) for num in block.split("\n")] for block in f.read().split("\n\n")]
  #print(array)
  # sum second dimension of the array into one number and store as list
  sum_list = list(map(sum,array))
  #print(sum_list)
  max_calorie_elf=max(sum_list)
  print(max_calorie_elf)