from itertools import pairwise, accumulate
from functools import reduce
import copy

def part_one(input_path: str) -> int:
  with open(input_path) as f:
    reports = [list(map(int,line.split(' '))) for line in f.read().split('\n')]

  count = 0
  for report in reports:
    count += 1 if is_safe(report) else 0
  return count

def part_two(input_path: str) -> str:
  with open(input_path) as f:
    reports = [list(map(int,line.split(' '))) for line in f.read().split('\n')]

  rectifiable = 0
  for report in reports:
    for i in range(len(report)):
      if is_safe([*report[:i], *report[i + 1 :]]):
        rectifiable += 1
        break

  return rectifiable

def is_safe(sequence: list) -> bool:
  is_monotonic = all(is_increasing(sequence)) or all(is_decreasing(sequence))
  is_between_differ = all(is_differ(sequence, 3))
  return is_monotonic and is_between_differ

def is_increasing(sequence: list) -> iter:
  return [a < b for a,b in pairwise(sequence)]

def is_decreasing(sequence: list) -> iter:
  return [a > b for a,b in pairwise(sequence)]

def is_differ(sequence: list, at_most: int = 3) -> iter:
  return [abs(a - b) <= at_most for a,b in pairwise(sequence)]

if __name__ == "__main__":
  input_path = './day_02/input.txt'
  print("====Part one====")
  print(part_one(input_path))
  print("====Part two====")
  print(part_two(input_path))