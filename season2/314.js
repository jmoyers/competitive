const verticalOrder = (root) => {
  if (!root) return [];
  
  const matrix = {}
  
  const dfs = (node, r = 0, c = 0) => {
    matrix[c] = matrix[c] ? matrix[c] : {};
    matrix[c][r] = matrix[c][r] ? matrix[c][r] : [];
    matrix[c][r].push(node.val)
    
    if (node.left) {
      dfs(node.left, r + 1, c - 1);
    }
    
    if (node.right) {
      dfs(node.right, r + 1, c + 1);
    }
  }
  
  dfs(root)
  
  const vert = Object.keys(matrix).map((n) => Number(n)).sort((a, b) => a - b);
  const vals = vert.map((c) => Object.values(matrix[c]));
  return vals.map((val) => val.reduce((level, vals) => level.concat(vals), []));
};
