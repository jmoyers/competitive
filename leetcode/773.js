// On a 2x3 board, there are 5 tiles represented by the integers 1 through 5,
// and an empty square represented by 0.
//
// A move consists of choosing 0 and a 4-directionally adjacent number and
// swapping it.
//
// The state of the board is solved if and only if the board is
// [[1,2,3],[4,5,0]].
//
// Given a puzzle board, return the least number of moves required so that the
// state of the board is solved. If it is impossible for the state of the board
// to be solved, return -1.
//
// Examples:
//
// Input: board = [[1,2,3],[4,0,5]]
// Output: 1
// Explanation: Swap the 0 and the 5 in one move.
//
// Input: board = [[1,2,3],[5,4,0]]
// Output: -1
// Explanation: No number of moves will make the board solved.
//
// Input: board = [[4,1,2],[5,0,3]]
// Output: 5
// Explanation: 5 is the smallest number of moves that solves the board.
// An example path:
// After move 0: [[4,1,2],[5,0,3]]
// After move 1: [[4,1,2],[0,5,3]]
// After move 2: [[0,1,2],[4,5,3]]
// After move 3: [[1,0,2],[4,5,3]]
// After move 4: [[1,2,0],[4,5,3]]
// After move 5: [[1,2,3],[4,5,0]]
//
// Input: board = [[3,2,4],[1,5,0]]
// Output: 14

// if you consider each game state in the board to be a node
// in a graph, you can find the shortest path to a winning
// game state by using plain old breadth first search (queue based)
//
// if you were interested in more than one game state you could use
// dijkstra, but that is not necessary because we're not looking
// for the shortest path to ALL nodes, just one
//
// if you encode the gamestate into a string, you can use a hash set
// to keep track of the visited nodes.
//
// I prefer we keep the game state as an array so we can more easily
// reason about the next available nodes in the graph of the game state
// - in other words, so we can use 4 if statements to keep track of
// 4 directional movements available to us rather than using string
// manipulation

const cloneSwap = (gameState, p1, p2) => {
  const newGameState = gameState.map((row) => row.slice());
  let tmp = newGameState[p1.r][p1.c];
  newGameState[p1.r][p1.c] = newGameState[p2.r][p2.c];
  newGameState[p2.r][p2.c] = tmp;
  return newGameState;
};

const slidingPuzzle = (start) => {
  const target = [
    [1, 2, 3],
    [4, 5, 0],
  ];
  const visited = {};

  const cols = 3;
  const rows = 2;

  let startZero = null;

  for (let r = 0; r < start.length; r++) {
    for (let c = 0; c < start[r].length; c++) {
      if (start[r][c] === 0) startZero = { r, c };
    }
  }

  if (!startZero) return -1;

  const ageMarker = { board: false, zero: false };

  const queue = [ageMarker, { board: start, zero: startZero }];

  let level = 0;

  const directions = [
    { r: 0, c: -1 }, // left
    { r: -1, c: 0 }, // up
    { r: 0, c: 1 }, // right
    { r: 1, c: 0 }, // down
  ];

  for (;;) {
    const { board: curr, zero: currZero } = queue.pop();

    // if we reach one of these markers, we're either advancing a bfs
    // level or we're at the end of the queue
    if (curr === false) {
      if (queue.length === 0) {
        return -1;
      }
      level++;
      // mark where the next bfs level ends
      queue.unshift(ageMarker);
      continue;
    }

    let isTarget = true;

    for (let i = 0; i < curr.length; i++) {
      for (let j = 0; j < curr[i].length; j++) {
        if (curr[i][j] !== target[i][j]) isTarget = false;
      }
    }

    if (isTarget) return level;

    visited[curr.map((r) => r.join("")).join("")] = true;

    // consider all of the 4-directionally connected gamestates
    for (const dir of directions) {
      // if we're off the board, skip
      const newZero = { r: currZero.r + dir.r, c: currZero.c + dir.c };

      if (newZero.r < 0 || newZero.r > rows - 1) continue;
      if (newZero.c < 0 || newZero.c > cols - 1) continue;

      const newBoard = cloneSwap(curr, currZero, newZero);

      const stringId = newBoard.map((r) => r.join("")).join("");

      // if we're visited, skip
      if (visited[stringId]) continue;

      queue.unshift({ board: newBoard, zero: newZero });
    }
  }
};

// let res = slidingPuzzle([
//   [4, 1, 2],
//   [5, 0, 3],
// ]);

let res = slidingPuzzle([
  [3, 2, 4],
  [1, 5, 0],
]);

console.log(res);
