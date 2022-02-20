/**
 * @param {string} s
 * @return {string}
 */
var minRemoveToMakeValid = function(s) {
  const stack = []; 
  const remove = new Set();
  
  for (let [i,c] of s.split("").entries()) {
    if (c === "(") {
      stack.push(i);
    } else if (c === ")") {
      if (stack.length === 0) {
        remove.add(i);
      } else {
        stack.pop();
      }
    }
  }
  
  while (stack.length) remove.add(stack.pop());
  
  return s.split("").filter((val, index) => !remove.has(index)).join("");
};
