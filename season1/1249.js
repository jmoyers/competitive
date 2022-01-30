// Given a string s of '(' , ')' and lowercase English characters.
//
// Your task is to remove the minimum number of parentheses ( '(' or ')', in any
// positions ) so that the resulting parentheses string is valid and return any
// valid string.
//
// Formally, a parentheses string is valid if and only if:
//
//     It is the empty string, contains only lowercase characters, or
//     It can be written as AB (A concatenated with B), where A and B are valid strings, or
//     It can be written as (A), where A is a valid string.
//
//
//
// Example 1:
//
// Input: s = "lee(t(c)o)de)"
// Output: "lee(t(c)o)de"
// Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
//
// Example 2:
//
// Input: s = "a)b(c)d"
// Output: "ab(c)d"
//
// Example 3:
//
// Input: s = "))(("
// Output: ""
// Explanation: An empty string is also valid.
//
// Example 4:
//
// Input: s = "(a(b(c)d)"
// Output: "a(b(c)d)"
//
//
//
// Constraincts:
//
//     1 <= s.length <= 10^5
//     s[i] is one of  '(' , ')' and lowercase English letters.
//

const minRemoveToMakeValid = (s) => {
  // normally to determine validity in brace matching you can use a stack
  // e.g. push ( onto the stack, if you are closing ), pop ( off the stack
  // and you have a matched set of braces. stack has to be empty at the end
  // of the validity check

  // here we can use a similar concept but get the index of a brace
  // if we encounter an unmatched closing bracket, we definitely remove it
  // if we fully search the string and we have unmatched opening braces, we
  // can assume that opening braces that are locally matched by nearest closing
  // brace are valid, and then whatever we're left with do not have a matching closing
  // brace and should be removed.

  // this should be 2 pass, so O(2n). we need to make sure we are using indexes
  // and not adding and removing from a string or array prematurely so we don't incur
  // lookup or array insert/removal costs on a per index basis

  // first pass, remove unmatched closing braces and make a list of "valid" opening braces
  let open = 0;
  let close = 0;
  let openIndexes = [];
  let valid = {};

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(") {
      openIndexes.push(i);
      valid[i] = false;
      open++;
    } else if (s[i] === ")") {
      if (open <= close) {
        valid[i] = false;
      } else {
        valid[openIndexes.pop()] = true;
        valid[i] = true;
        close++;
      }
    } else {
      valid[i] = true;
    }
  }

  // build string now that we no which are valid
  let newString = "";
  for (let i = 0; i < s.length; i++) {
    if (valid[i]) newString += s[i];
  }
  return newString;
};

//const res = minRemoveToMakeValid("lee(t(c)o)de)");
//const res = minRemoveToMakeValid("a)b(c)d");
const res = minRemoveToMakeValid("))((");

console.log(res);
