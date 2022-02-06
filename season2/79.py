class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # graph as defined by horizontal and vertical connections
        # dfs can be used
        # trie could be used, but we can prob just use the array since
        # there is only one word!
        if not board:
            return False if not word else True
        
        self.y = len(board) 
        self.x = len(board[0]) 
        
        for y in range(self.y):
            for x in range(self.x):
                if self.dfs(board, x, y, word, 0):
                    return True
                
        return False
    
    def dfs(self, board, x, y, word, i):
        if i == len(word):
            return True
        
        if x > self.x - 1 or x < 0:
            return False
        
        if y > self.y - 1 or y < 0:
            return False
        
        if word[i] != board[y][x]:
            return False
        
        tmp, board[y][x] = board[y][x], '-'
        
        #print(f'{x},{y}: {seen} {word[0:i]}')
        
        # check left
        if self.dfs(board, x-1, y, word, i+1):
            return True
        
        # check right
        if self.dfs(board, x+1, y, word, i+1):
            return True
        
        # check down
        if self.dfs(board, x, y+1, word, i+1):
            return True
        
        # check up
        if self.dfs(board, x, y-1, word, i+1):
            return True
        
        board[y][x] = tmp
        return False
