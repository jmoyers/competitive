// Given a 2d grid map of '1's (land) and '0's (water), count the number of
// islands. An island is surrounded by water and is formed by connecting
// adjacent lands horizontally or vertically. You may assume all four edges of
// the grid are all surrounded by water.
//
// Example 1:
//
// Input:
// 11110
// 11010
// 11000
// 00000
//
// Output: 1
//
// Example 2:
//
// Input:
// 11000                 111000
// 11000                 001000
// 00100                 001100 2
// 00011                 000010
//
// Output: 3

// loop through all positions, making note of land that is found. if this
// is the first time we've encountered land, mark this on a map as island 1
// continue to loop, if we encounter more land, we check its 4 connecting
// squares around it. if we find land that is already classified, inherit its
// indentifier, otherwise its a new island

const numIslands = grid => {
  if (grid.length === 0) return 0;
  if (grid[0].length === 0) return 0;
  const nr = grid.length;
  const nc = grid[0].length;
  let islands = 0;

  const dfs = (grid, r, c) => {
    grid[r][c] = "0";
    // top
    if (r - 1 >= 0 && grid[r - 1][c] === "1") dfs(grid, r - 1, c);
    // left
    if (c - 1 >= 0 && grid[r][c - 1] === "1") dfs(grid, r, c - 1);
    // right
    if (r + 1 < nr && grid[r + 1][c] === "1") dfs(grid, r + 1, c);
    // bottom
    if (c + 1 < nc && grid[r][c + 1] === "1") dfs(grid, r, c + 1);
  };

  for (let r = 0; r < nr; r++) {
    for (let c = 0; c < nc; c++) {
      if (grid[r][c] === "1") {
        islands++;
        // clear the rest of the attached island using dfs
        dfs(grid, r, c);
      }
    }
  }

  return islands;
};

console.log(
  numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
  ])
);

console.log(
  numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
  ])
);

console.log(
  numIslands([
    ["1", "1", "1"],
    ["0", "1", "0"],
    ["1", "1", "1"]
  ])
);

console.log(
  numIslands([
    ["1", "1", "1", "1", "1", "1", "1"],
    ["0", "0", "0", "0", "0", "0", "1"],
    ["1", "1", "1", "1", "1", "0", "1"],
    ["1", "0", "0", "0", "1", "0", "1"],
    ["1", "0", "1", "0", "1", "0", "1"],
    ["1", "0", "1", "1", "1", "0", "1"],
    ["1", "1", "1", "1", "1", "1", "1"]
  ])
);
