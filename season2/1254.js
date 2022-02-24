/**
 * @param {number[][]} grid
 * @return {number}
 */
const closedIsland = (grid) => {
  const N = grid.length;
  const M = grid[0].length;
  let ans = 0;
  const visited = new Set();

  const has_visited = (r, c) => {
    return visited.has(`${r},${c}`);
  };

  let found_land = false;

  const dfs = (r, c) => {
    if (r >= N || r < 0 || c >= M || c < 0 || has_visited(r, c)) {
      //console.log('edge of map or visited');
      return false;
    }

    if (grid[r][c] === 0) {
      visited.add(`${r},${c}`);
      found_land = true;
    }

    //console.log(r, c, grid[r][c], found_land);

    if (grid[r][c] === 1) {
      if (found_land) {
        //console.log('found water after land');
        return true;
      }
      return false;
    }

    let closed_island = true;

    if (!has_visited(r - 1, c) && !dfs(r - 1, c)) closed_island = false;
    if (!has_visited(r + 1, c) && !dfs(r + 1, c)) closed_island = false;
    if (!has_visited(r, c - 1) && !dfs(r, c - 1)) closed_island = false;
    if (!has_visited(r, c + 1) && !dfs(r, c + 1)) closed_island = false;

    return closed_island;
  };

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      found_land = false;
      if (dfs(i, j)) {
        ans += 1;
        //console.log(i, j);
      }
      //console.log();
    }
  }

  return ans;
};
