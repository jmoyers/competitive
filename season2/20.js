/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
  // ()(()())
  // 
  
  const stack = [];
  const opens = new Set(['(', '{', '[']);
  
  for (const c of s) {
    if (opens.has(c)) {
      stack.push(c);
      continue;
    } else if (stack.length) {
      if (c === ')' && stack.pop() === '(') continue;
      if (c === '}' && stack.pop() === '{') continue;
      if (c === ']' && stack.pop() === '[') continue;
      return false;
    } else {
      return false;
    }
  }
  
  return stack.length === 0;
};
