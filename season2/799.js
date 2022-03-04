/**
 * @param {number} poured
 * @param {number} query_row
 * @param {number} query_glass
 * @return {number}
 */
const champagneTower = (poured, query_row, query_glass) => {
  const glasses = new Array(101)
    .fill(0)
    .map((v, i) => new Array(i + 1).fill(0));

  // treat each glass as "how much has passed through" rather than how much it holds.

  // iterate and for each glass, keep track of how much we pour into the two child glasses

  // children glasses[r][c]
  // glasses[r+1][c], glasses[r+1][c+1]

  glasses[0][0] = poured;

  for (let r = 0; r <= query_row; r++) {
    for (let c = 0; c <= r; c++) {
      const pour_down = Math.max(0, (glasses[r][c] - 1) / 2);
      glasses[r + 1][c] += pour_down;
      glasses[r + 1][c + 1] += pour_down;
    }
  }

  //console.log('poured', poured, 'query_row', query_row, 'query_glass', query_glass);
  //console.log(glasses.slice(0, query_row + 1));

  return Math.min(1, glasses[query_row][query_glass]);
};
