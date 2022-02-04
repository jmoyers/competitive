from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for word in strs:
            counted = Counter(word)
            groups[frozenset(counted.items())].append(word)
        
        return list(groups.values())
                
