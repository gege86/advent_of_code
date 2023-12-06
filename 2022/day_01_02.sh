#!/bin/bash 

# get the sum of calories for the 3 elves carrying the top3 most calories

#set -x

max_elf_cal_01=0
max_elf_cal_02=0
max_elf_cal_03=0
current_elf_cal=0

while read line; do
  if [ -z "$line" ]; then
    if [ "$max_elf_cal_01" -le "$current_elf_cal" ]; then
      max_elf_cal_03=$max_elf_cal_02
      max_elf_cal_02=$max_elf_cal_01
      max_elf_cal_01=$current_elf_cal
    elif [ "$max_elf_cal_02" -le "$current_elf_cal" ]; then
      max_elf_cal_03=$max_elf_cal_02
      max_elf_cal_02=$current_elf_cal
    elif [ "$max_elf_cal_03" -le "$current_elf_cal" ]; then
      max_elf_cal_03=$current_elf_cal
    fi
    current_elf_cal=0
  else
    current_elf_cal=$(($current_elf_cal + $line))
  fi
done < list.txt

sum_top3_cal=$(($max_elf_cal_01 + $max_elf_cal_02 + $max_elf_cal_03))
echo "The summ of calories for the 3 elves carrying the top3 most calories is $sum_top3_cal calories."