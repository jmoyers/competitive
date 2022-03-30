/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function (matrix, target) {
  const flattened = matrix.reduce((acc, arr) => acc.concat(arr), []);

  const binarySearch = (arr, target, start = 0, end = arr.length - 1) => {
    if (start > end) return false;
    const mid = Math.floor((end - start) / 2 + start);
    if (arr[mid] === target) return true;
    if (arr[mid] > target) {
      return binarySearch(arr, target, start, mid - 1);
    } else {
      return binarySearch(arr, target, mid + 1, end);
    }
  };

  return binarySearch(flattened, target);
};
