from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # seems like a graph
        # edges are between words with one charcter difference
        # the shortest implies a bfs
        # building adj list is iterating over every word in wordList
        # check total differences, if diff == 1, add edge
        # check if endWord in word list
        # bfs from beginWord, find endWord, count levels
        
        if endWord not in wordList:
            return 0
        
        generic_adj = defaultdict(set)
        adj = defaultdict(set)
        
        wordList.append(beginWord)
        
        for word in wordList:
            for i in range(len(word)):
                generic = f'{word[0:i]}#{word[i+1:]}'
                
                generic_adj[generic].add(word)
       
        adj = defaultdict(list)
        
        for generic, words in generic_adj.items():
            for word in words:
                adj[word] += set(words)
                
        queue = deque([beginWord, "*"])
        level = 1
        
        seen = set()
        
        #print(adj)
        
        while len(queue) > 1:
            node = queue.popleft()
            
            #print(node, queue)
            
            if node in seen: continue
            
            if node == "*":
                level += 1
                queue.append('*')
                continue
            
                
            if node == endWord:
                return level
            
            seen.add(node)
            
            queue.extend(adj[node])
            
        return 0
