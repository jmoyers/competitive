import copy

class TrieNode:
    def __init__(self):
        self.map = {}
        self.word_boundary = False
    
    def next(self, c):
        if c in self.map:
            return self.map[c]
        else:
            return False
    
    def add(self, word):
        curr = self.map

        for c in word:
            if c in curr:
                curr = curr[c]
            else:
                curr[c] = TrieNode()
                curr = curr[c]
        
        curr.word_boundary = True

class Solution:
    def originalDigits(self, s):
        options = {
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
        }

        trie = TrieNode()

        for num in options:
            trie.add(options[num])
        
        output = []

        self._recurse(s, trie, output)

        output.sort()

        string_output = ""

        for num in output:
            string_output += num
        
        return string_output

        # approach 1, listed here, unfinished, bad
        # out of order characters
        # this is a permutations problem
        # set of the valid characters from the string
        # the tree of possibilities starts with with removing character from the
        # set and then resolving all possible versions of the string
        # we can solve for any valid permutation and then sort the resulting
        # number array

        # approach 2 is something that was pretty unintuive for me, and i will
        # take a break on this problem for now
        # you need to look at the letters that are unique in each number
        # ascending. you'll find half of them have unique letters so that if
        # those letters are present, there are n instances of that number. from
        # there you can build simple representation of the remaining letters by
        # looking for the least frequently occuring letter per number word, and
        # then subtracting the count of that letter from the known word counts
        # where the letter previously is known to have occured. its a little
        # goofy to understand with just words, but if you draw it out it becomes
        # somewhat obvious. i am taking a break from this problem because its a
        # "gotcha" style problem and doesn't have a general computer science 
        # application

        # i believe we can use trie data structure to keep track of the possible
        # permutations of letters for the next remove from set/recurse

        # create a trie from all the available number-words

        # recurse start
        # start at position 1, take character from position 1 enter trie
        # not a word, not done with the input
        # take a character from positions curr + 1 -> end recurse

        # base cases
        # * input string is not empty, and we ARE at a word boundary, and this
        #   is a valid child of current trie, recurse and reset trie state
        # * input string is empty and we ARE at a word boundary, return this
        #   number set
        # * input string is empty and we are not at a word boundary per trie,
        #   this branch of the tree is not valid
        # * this character we're examining isn't in the children of the trie,
        #   this branch of the tree is not valid
        # * input string is not empty, and we are not at a word boundary, but
        #   this is a valid child of current trie, recurse and keep trie state
    
    def _recurse(s, trie, output):
        for i, c in enumerate(s):
            curr = trie.next(c)

            if curr and curr.word_boundary and len(s) > 1:
                new_input = s[0:i-1] + s[i+1:]
                new_output = copy.copy(output)
                if self._recurse(new_input, curr, new_output):
                    




