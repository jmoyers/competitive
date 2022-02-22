/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function (board) {
  // iterate through each row
  // iterate through each column
  // iterate through the 9 grids
  // make sure no duplicates for a 1 - 9 set
  // use javascript Set
  // empty is okay - dot is empty

  for (const row of board) {
    const set = new Set();
    for (const val of row) {
      if (val === ".") continue;
      if (set.has(val)) return false;
      set.add(val);
    }
  }

  for (let x = 0; x < board.length; x++) {
    const set = new Set();
    for (let y = 0; y < board[0].length; y++) {
      const val = board[y][x];
      if (val === ".") continue;
      if (set.has(val)) return false;
      set.add(val);
    }
  }

  for (let gridX = 0; gridX <= 6; gridX += 3) {
    for (let gridY = 0; gridY <= 6; gridY += 3) {
      const set = new Set();

      for (let currX = 0; currX < 3; currX++) {
        for (let currY = 0; currY < 3; currY++) {
          const val = board[currX + gridX][currY + gridY];
          if (val === ".") continue;
          if (set.has(val)) return false;
          set.add(val);
        }
      }
    }
  }

  return true;
};
