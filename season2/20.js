/**
 * @param {string} s
 * @return {boolean}
 */
const isValid = (s) => {
  const stack = [];
  
  for (const c of s) {
    
    if (c === "(" || c === "[" || c === "{") {
      stack.push(c);
    }
    
    if (c === ")" && stack.length && stack[stack.length - 1] === "(") {
      stack.pop();
    } else if (c === ")") {
      return false;
    }
    
    
    if (c === "}" && stack.length && stack[stack.length - 1] === "{") {
      stack.pop();
    } else if (c === "}") {
      return false;
    }
    
    if (c === "]" && stack.length && stack[stack.length - 1] === "[") {
      stack.pop();
    } else if (c === "]") {
      return false;
    }
  }
  
  return stack.length === 0;
};
