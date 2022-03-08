/**
 * @param {number[]} answers
 * @return {number}
 */
var numRabbits = function (answers) {
  const map = {};

  for (const a of answers) {
    if (map[a + 1]) {
      map[a + 1]++;
    } else {
      map[a + 1] = 1;
    }
  }

  return Object.entries(map).reduce((min, [k, v]) => {
    return min + Math.max(Math.ceil(v / k) * k, k);
  }, 0);
};
