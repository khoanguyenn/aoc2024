import re

def part_one(input_path: str):
  with open(input_path) as f:
    lines = f.read()

  products = [int(x) * int(y) for (x, y) in re.findall(r'mul\((\d*),(\d*)\)', lines)]
  return sum(products)

def part_two(input_path: str):
  with open(input_path) as f:
    lines = f.read()
    
  matches = re.finditer(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)", lines)
  result = 0
  enabled = True
  for match in matches:
    command, a, b = match.group(0, 1, 2)
    if command == "do()":
      enabled = True
    elif command == "don't()":
      enabled = False
    elif enabled:
      result += int(a) * int(b)
    else:
      pass
  return result

if __name__ == "__main__":
  input_path = './day_03/input.txt'
  print("====Part one====")
  print(part_one(input_path))
  print("====Part two====")
  print(part_two(input_path))
