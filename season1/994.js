// In a given grid, each cell can have one of three values:
//
//   the value 0 representing an empty cell;
//   the value 1 representing a fresh orange;
//   the value 2 representing a rotten orange.
//
// Every minute, any fresh orange that is adjacent (4-directionally) to a
// rotten orange becomes rotten.
//
// Return the minimum number of minutes that must elapse until no cell has a
// fresh orange.  If this is impossible, return -1 instead.
//
// Example 1:
//
// Input: [[2,1,1],[1,1,0],[0,1,1]]
// Output: 4
//
// Example 2:
//
// Input: [[2,1,1],[0,1,1],[1,0,1]]
// Output: -1
// Explanation:  The orange in the bottom left corner (row 2, column 0) is
// never rotten, because rotting only happens 4-directionally.
//
// Example 3:
//
// Input: [[0,2]]
// Output: 0
// Explanation:  Since there are already no fresh oranges at minute 0, the
// answer is just 0.
//
// Note:
//
//     1 <= grid.length <= 10
//     1 <= grid[0].length <= 10
//     grid[i][j] is only 0, 1, or 2.
//

// first add all of the rotting oranges to a bfs queue
// once this entire queue is processed, 1 minute has passed
//
// we can count the number of fresh oranges on the first iteration,
// and subtract them when we rot an orange out, in this way we save having
// to iterate over the again (even though this is still O(n))
//
// because we use a queue structure and keep track of each "phase" (e.g. the
// current depth of the bfs search from its root nodes), we are able to
// keep track of the minutes passed as all rot is happening "simultaneously"
// from each rotting root node
const orangesRotting = grid => {
  const rows = grid.length;
  const cols = grid[0].length;
  const queue = [];
  const visited = {};
  const rotted = 2,
    fresh = 1;
  let freshOranges = 0;
  let minutes = 0;

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (grid[r][c] === rotted) {
        queue.unshift([r, c]);
      }

      if (grid[r][c] === fresh) freshOranges++;
    }
  }

  // reach this and first minute is over
  queue.unshift([-1, -1]);

  while (queue.length && freshOranges) {
    let node = queue.pop();
    let r = node[0],
      c = node[1];

    if (visited[r * cols + c]) continue;

    if (r === -1) {
      minutes++;
      // if there is any more work to process after this minute has passed
      // track another minute, or else leave the queue empty
      if (queue.length) queue.unshift([-1, -1]);
      continue;
    }

    visited[r * cols + c] = true;
    if (grid[r][c] === fresh) {
      grid[r][c] = 2;
      freshOranges--;
    }

    // 4-directionally check surrounding area for fresh oranges
    if (r - 1 >= 0 && grid[r - 1][c] === fresh) queue.unshift([r - 1, c]);
    if (r + 1 < rows && grid[r + 1][c] === fresh) queue.unshift([r + 1, c]);
    if (c - 1 >= 0 && grid[r][c - 1] === fresh) queue.unshift([r, c - 1]);
    if (c + 1 < cols && grid[r][c + 1] === fresh) queue.unshift([r, c + 1]);
  }

  return freshOranges === 0 ? minutes : -1;
};

console.log(
  orangesRotting([
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
  ])
);

// Output: 4
console.log(
  orangesRotting([
    [2, 1, 1],
    [0, 1, 1],
    [1, 0, 1]
  ])
);
// Output: -1
