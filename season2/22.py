class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # this problem can be represented by recursion with:
        # choices:
        #   place an open bracket
        #   place a close bracket
        # contraints:
        #   you can't place a close bracket if you haven't placed an equal number
        #       open brackets
        #   you can't open if there isn't at least one more open space to close
        # state:
        #   open bracket count
        #   close bracket count
        #   string so far
        #   remaining space count
        #   results
        # base cases:
        #   n = 0, empty set and if we reach n = 0 with equal open/close count it is valid
        #   if n = 0, and we have an unequal open/close count, solution is not valid
        # memoize:
        #   solutions for smaller n, use this when you have an even open/close and n remaining
        self.memo = {}
        
        results = []
        
        self._recurse(0, 0, n * 2, "", results);
        
        return results
    
    def _recurse(self, open_count, close_count, remaining_space, result, results = []):
        if open_count == close_count and remaining_space == 0:
            results.append(result)
        elif open_count != close_count and remaining_space == 0:
            return False
        
        choices = []
        
        if open_count > close_count:
            choices.append(")")
        if open_count - close_count < remaining_space - 1:
            choices.append("(")
        
        for choice in choices:
            if choice == "(":
                self._recurse(open_count + 1, close_count, remaining_space - 1, result + "(", results)
            else:
                self._recurse(open_count, close_count + 1, remaining_space - 1, result + ")", results)
