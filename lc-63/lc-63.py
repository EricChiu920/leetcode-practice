from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
      if obstacleGrid[0][0] == 1: return 0
      
      m = len(obstacleGrid)
      n = len(obstacleGrid[0])

      grid = [[0] * n for i in range(m)]
      grid[0][0] = 1

      for row in range(m):
        for col in range(n):
          if obstacleGrid[row][col] == 1: continue
          if row > 0:
            grid[row][col] += grid[row - 1][col]
          if col > 0:
            grid[row][col] += grid[row][col - 1]

      return grid[m - 1][n - 1]
