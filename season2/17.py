class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        self.n = len(digits)
        self.char_map = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }
        
        ans = []
        self.dfs(digits, [], ans)
        return ans
    
    def dfs(self, choices, path, ans):
        if len(path) == self.n:
            ans.append("".join(path))
            return
        
        # choose a number and get the letters for number
        for i, n in enumerate(choices):
            for c in self.char_map[int(n)]:
                self.dfs(choices[i+1:], path+[c], ans)
