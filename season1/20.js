// Given a string containing just the characters '(', ')', '{', '}', '[' and
// ']', determine if the input string is valid.
//
// An input string is valid if:
//
//     Open brackets must be closed by the same type of brackets.
//     Open brackets must be closed in the correct order.
//
// Note that an empty string is also considered valid.
//
// Example 1:
//
// Input: "()"
// Output: true
//
// Example 2:
//
// Input: "()[]{}"
// Output: true
//
// Example 3:
//
// Input: "(]"
// Output: false
//
// Example 4:
//
// Input: "([)]"
// Output: false
//
// Example 5:
//
// Input: "{[]}"
// Output: true
//

// this is the exact property that a stack gives to us
const isValid = s => {
  const stack = [];
  const validMap = { "(": ")", "{": "}", "[": "]" };
  for (let c of s) {
    if (c === "(" || c === "{" || c === "[") {
      stack.push(c);
    } else {
      if (c !== validMap[stack.pop()]) return false;
    }
  }
  return stack.length === 0;
};

console.log(isValid("{[]}"));
console.log(isValid("([)]"));
