//  Given n pairs of parentheses, write a function to generate all combinations
//  of well-formed parentheses.
//
// For example, given n = 3, a solution set is:
//
// [
//   "((()))",
//   "(()())",
//   "(())()",
//   "()(())",
//   "()()()"
// ]

const generateParenthesis = n => {
  const result = [];

  const backtrack = (curr = "", open = 0, close = 0, max = n * 2) => {
    if (curr.length === max) {
      result.push(curr);
      return;
    }

    if (open < max / 2) backtrack(curr + "(", open + 1, close, max);
    if (close < open) backtrack(curr + ")", open, close + 1, max);
  };

  backtrack();
  return result;
};

generateParenthesis(3);
