#!/bin/bash 

#set -x

max_elf_cal=0
current_elf_cal=0

while read line; do
  if [ -z "$line" ]; then
    if [ "$max_elf_cal" -lt "$current_elf_cal" ]; then
      max_elf_cal=$current_elf_cal
    fi
    current_elf_cal=0
  else
    current_elf_cal=$(($current_elf_cal + $line))
  fi
done < list.txt

echo "Elf with most calories has $max_elf_cal calories."
