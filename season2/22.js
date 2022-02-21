const generateParenthesis = function(n) {
  const dfs = (open, close, path, ans) => {
    //console.log(open, close, path, ans)
    if (path.length === n*2) {
      if (open === close) ans.push(path.join(""));
      return;
    }
    
    if ((open - close) > (n*2) - path.length) return;
    
    if (open > close) {
      path.push(")");
      dfs(open, close + 1, path, ans);
      path.pop();
    } 
    
    if (open >= close) {
      path.push("(");
      dfs(open + 1, close, path, ans);
      path.pop();
    }
  }
  
  const ans = [];
  
  dfs(0,0,[],ans);
  
  return ans;
};
