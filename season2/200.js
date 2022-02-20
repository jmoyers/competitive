/**
 * @param {character[][]} grid
 * @return {number}
 */
const numIslands = (grid) => {
  // graph problem - horiz/vertical land are adjacent nodes
  // visit all nodes, and keep track of how many connected components = islands
  // visited set to keep track of where we've been (Set, member is a tuple of x, y)
  // keep track of visited set directly in graph to use no extra space -- set the value
  // to some non-1 value to indicate we've already visited
  // dfs
  
  
  // start iteration from any point, visit all connected nodes from that point, continue iteration
  if (!grid.length) return 0;
  if (!grid[0].length) return 0;
  
  const dfs = (row, column) => {
    //console.log(row, column);
    if (grid[row][column] === '1') {
      grid[row][column] = '#';
      
      // up
      if (row >= 1) {
        dfs(row - 1, column);
      }
      
      // down
      if (row < n - 1) {
        dfs(row + 1, column);
      }
      
      // left
      if (column >= 1) {
        dfs(row, column - 1);
      }
      
      // right
      if (column < m - 1) {
        dfs(row, column + 1);
      }
      
      return true;
    } else {
      return false;
    }
  }

  
  const n = grid.length, m = grid[0].length;
  let ans = 0;
  
  for (let row = 0; row < n; row++) {
    for (let column = 0; column < m; column++) {
      if (dfs(row, column)) {
        ans += 1;
      }
    }
  }
  
  
  return ans;
};
