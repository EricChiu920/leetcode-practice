# iterative soltion with tabulation
class Solution:
  def uniquePaths(self, m: int, n: int, memo=None) -> int:
    grid = [[0] * n for i in range(m)]

    grid[0][0] = 1

    for row in range(m):
      for col in range(n):
        if row > 0:
          grid[row][col] += grid[row - 1][col]
        if col > 0:
          grid[row][col] += grid[row][col - 1]

    return grid[m - 1][n - 1]
