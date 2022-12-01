
# get the sum of calories for the 3 elves carrying the top3 most calories

# read stuff into 2 dimensional array(?) - thanks stackoverflow
with open('list.txt') as f:
  array = [[int(num) for num in block.split("\n")] for block in f.read().split("\n\n")]
  #print(array)
  # sum second dimension of the array into one number and store as list
  sum_list = list(map(sum,array))
  #print(sum_list)
  # https://stackoverflow.com/questions/10152131/how-do-i-index-the-3-highest-values-in-a-list
  print(sorted(sum_list, reverse=True)[:3])
  solution = sum(sorted(sum_list, reverse=True)[:3])
  print("Solution is: " + str(solution))