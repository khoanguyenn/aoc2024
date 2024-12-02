import heapq
from collections import defaultdict

def part_one(filename: str) -> int:
  group_1, group_2 = read_locations(filename)
  heapq.heapify(group_1), heapq.heapify(group_2)

  distances = [abs(heapq.heappop(group_1) - heapq.heappop(group_2)) for _ in range(len(group_1))]
  return sum(distances)

def part_two(filename: str) -> int:
  group_1, group_2 = read_locations(filename)
  seen = defaultdict(int)

  for locat in group_2: seen[locat] += 1

  similarity = [locat*seen[locat] for locat in group_1]
  return sum(similarity)

def read_locations(filename: str) -> tuple[list, list]:
  group_1, group_2 = [], []
  with open(filename, 'r') as f:
    for line in f:
      locat1, locat2 = map(int, line.strip().split('   '))
      group_1.append(locat1)
      group_2.append(locat2)
  return group_1, group_2

if __name__ == "__main__":
  input_path = './day_01/input.txt'
  print("====Part one====")
  print(part_one(input_path))
  print("====Part two====")
  print(part_two(input_path))
