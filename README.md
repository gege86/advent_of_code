# advent_of_code_2022
https://adventofcode.com/2022/
### What I learned
* python creates blocks by indentation - no need to end block with keyword
* if statement equality comparison is done by == and ends in :
* print("hello") to print stuff
* print("my age is" + str(4)) to print integers concatenated with string
* you can easily read in a whole text file and split it into a list line by line
```
with open('input.txt') as f:
  my_list = f.read().split("\n")
```
* you can do block comments with """ bla bla line break etc. bla bla """
* some cool data types:
  * list
    * like an array, but takes up more space
    * (no built-in array data type in python btw)
    * items in the list
      * are ordered
      * are changeable
      * allow duplicate values
      * can have various data types (stuff can be nested)
    * you can pop/append elements from/to it (treat it like a "stack")
    * can be converted into a set
  * set
    * can be used to do set-like comparisons, like
    * check if a set contains another
* TO DO list comprehension (add example)
* TO DO dictionary comprehension (add example)
* TO DO add recursive function types
* TO DO for else