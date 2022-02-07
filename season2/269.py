from collections import defaultdict

class Solution:
    def has_cycle(self, node, seen):
        if node in seen: return True
        if not node: return False
        
        seen.add(node)
        
        for child in self.adj[node]:
            if self.has_cycle(child, seen.copy()):
                return True
        
        return False
        
    def dfs(self, node, seen, topo):
        if node in seen:
            return
        
        children = [child for child in self.adj[node] if child not in seen]
        
        seen.add(node) 
        
        for child in children:
            self.dfs(child, seen, topo)
        
        topo.append(node)
        
    def alienOrder(self, words: List[str]) -> str:
        if len(words) == 1:
            return "".join(list(set(words[0])))
        # create a DAG from the words, such that we map
        # the relative order in the word
        # do a topological sort
        # reverse the topological sort
        
        # build adj list
        self.adj = defaultdict(set)
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            
            if word1 == word2: 
                for c in word1:
                    self.adj[c] = set()
                continue
            
            for c in word1 + word2:
                if c not in self.adj:
                    self.adj[c] = set()
            
            index = 0
            
            size = min(len(word1), len(word2)) - 1
            
            while index < size and word1[index] == word2[index]:
                index += 1
            
            if index > 0 and index == size and len(word1) > len(word2) and word1[0:index+1] == word2[0:index+1]:
                return ""
            
            self.adj[word1[index]].add(word2[index])
        
        seen = set()
        topo = []
        
        nodes = list(self.adj.keys())
        
        if not nodes or self.has_cycle(nodes[0], set()):
            return ""
        
        for node in nodes:
            if node not in seen:
                self.dfs(node, seen, topo)
        
        return "".join(reversed(topo))
