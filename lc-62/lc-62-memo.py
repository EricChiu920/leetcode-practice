# recursive solution memoization
class Solution:
  def uniquePaths(self, m: int, n: int, memo = None) -> int:
    if memo is None: memo = {}
    key1 = (m, n)
    key2 = (n, m)

    if key1 in memo or key2 in memo: return memo[key1] 
    if m == 1 or n == 1: return 1

    memo[key1] = self.uniquePaths(m - 1, n, memo) + self.uniquePaths(m, n - 1, memo)
    memo[key2] = memo[key1]

    return memo[key1]
