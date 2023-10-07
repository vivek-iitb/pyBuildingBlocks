#https://leetcode.com/problems/number-of-islands/

def numIslands(self, grid: List[List[str]]) -> int:
  for row in grid:
    for col in grid[row]:
      if grid[col][row] = 1:
        augment =
      else


''' Definition of island: 1s surrounded by 0, every node connected to the 1 is 0'''


def count_set (x):
  count=0
  while x:
    count+= x&1
    x>>=1
  return count

print(count_set(10))

