class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        # markov chain
        # can use a table of probabilities that we need to keep two stages for
        # a1 = step - 1, a2 = step
        
        a1 = [[0] * N for _ in range(N)]
        a2 = [[0] * N for _ in range(N)]
        
        a1[r][c] = 1
        
        moves = [
          (2, 1),
          (1, 2),
          (-1, 2),
          (-2, 1),
          (2, -1),
          (1, -2),
          (-1, -2),
          (-2, -1)
        ]
        
        for k in range(0, K):
          for i in range(N):            
            for j in range(N):
              for R, C in moves:
                R, C = i + R, j + C
                if R >= 0 and R < N and C >= 0 and C < N:
                  a2[R][C] += a1[i][j] * (1/8)
                  
          a1 = a2
          a2 = [[0] * N for _ in range(N)]
        
        
        ans = 0
        
        print(a1)
        
        for i in range(N):
          for j in range(N):
            ans += a1[i][j]
            
        return ans
              
              
        
        
