/**
 * @param {number} length
 * @param {number[][]} updates
 * @return {number[]}
 */
const getModifiedArray = (length, updates) => {
  const arr = new Array(length);
  arr.fill(0);

  if (!updates.length) return arr;

  for (const update of updates) {
    for (let i = update[0]; i <= update[1]; i++) {
      arr[i] += update[2];
    }
  }

  return arr;
};
