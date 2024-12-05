
word = 'XMAS'

def part_one(input_path: str):
  with open(input_path) as file:
    grid = [list(line.strip()) for line in file]

  rows = len(grid)
  cols = len(grid[0])
  word_len = len(word)
  directions = [
    (-1, 0), #u
    (1, 0), #d
    (0, -1), #l
    (0, 1), #r
    (-1, -1), #ul
    (-1, 1), #ur
    (1, -1), #dl
    (1, 1), #dr
  ]

  def is_valid(r, c):
    return 0 <= r < rows and 0 <= c < cols

  def is_matched(r, c, dr, dc):
    for i in range(word_len):
      nr, nc = r + i * dr, c + i * dc
      if not is_valid(nr, nc) or grid[nr][nc] != word[i]:
        return False
    
    return True

  count = 0
  for r in range(rows):
    for c in range(cols):
      for dr, dc in directions:
        if is_matched(r, c, dr, dc):
          count += 1

  return count

def part_two(input_path: str):
  with open(input_path, 'r') as file:
    grid = [list(line.strip()) for line in file]

  rows, cols = len(grid), len(grid[0])
  _set = {'S', 'M'}

  count = 0
  for r in range(1, rows - 1):
    for c in range(1, cols - 1):
      if grid[r][c] == 'A':
        if {grid[r - 1][c - 1], grid[r + 1][c + 1]} == _set and {grid[r - 1][c + 1], grid[r + 1][c - 1]} == _set:
          count += 1

  return count

if __name__ == "__main__":
  input_path = './day_04/input.txt'
  print("Part one:", part_one(input_path))
  print("Part two:", part_two(input_path))
