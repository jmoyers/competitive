class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # dfs solution
        ans = []
        self.dfs(nums, [], ans)
        return ans
    
    def dfs(self, choices, path, ans):
        ans.append(path)
        
        for i, n in enumerate(choices):
            # progressively removing choices
            self.dfs(choices[i+1:], path + [n], ans)
    
