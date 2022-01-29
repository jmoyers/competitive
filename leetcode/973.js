// We have a list of points on the plane. Find the K closest points to the
// origin (0, 0).
//
// (Here, the distance between two points on a plane is the Euclidean distance.)
//
// You may return the answer in any order. The answer is guaranteed to be unique
// (except for the order that it is in.)
//
//
//
// Example 1:
//
// Input: points = [[1,3],[-2,2]], K = 1
// Output: [[-2,2]]
// Explanation:
// The distance between (1, 3) and the origin is sqrt(10).
// The distance between (-2, 2) and the origin is sqrt(8).
// Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
// We only want the closest K = 1 points from the origin, so the answer is just
// [[-2,2]].
//
// Example 2:
//
// Input: points = [[3,3],[5,-1],[-2,4]], K = 2
// Output: [[3,3],[-2,4]]
// (The answer [[-2,4],[3,3]] would also be accepted.)
//
// Note:
//
//     1 <= K <= points.length <= 10000
//     -10000 < points[i][0] < 10000
//     -10000 < points[i][1] < 10000
//
//

class MaxHeap {
  constructor() {
    this.store = [];
    this.comparator = (a, b) => {
      if (typeof b === "undefined") return true;
      if (a.dist > b.dist) return true;
      return false;
    };
  }
  swap(a, b) {
    const tmp = this.store[b];
    this.store[b] = this.store[a];
    this.store[a] = tmp;
  }
  insert(p) {
    this.store.push(p);

    let index = this.store.length - 1;
    let parent = Math.floor((index - 1) / 2);
    let swapped = true;

    while (parent >= 0 && swapped) {
      swapped = false;

      if (this.comparator(this.store[index], this.store[parent])) {
        this.swap(index, parent);
        swapped = true;
        index = parent;
        parent = Math.floor((index - 1) / 2);
      }
    }
  }
  extract() {
    if (this.store.length === 0) return false;
    if (this.store.length === 1) return this.store.pop();

    this.swap(0, this.store.length - 1);

    const min = this.store.pop();

    let shouldSwap = true;

    let index = 0;
    let [left, right] = [index * 2 + 1, index * 2 + 2];

    while (this.store[left] && shouldSwap) {
      const isLeftCandidate = this.comparator(
        this.store[left],
        this.store[right]
      );

      const candidate = isLeftCandidate ? left : right;
      shouldSwap = !this.comparator(this.store[index], this.store[candidate]);

      if (shouldSwap) {
        this.swap(index, candidate);
        index = candidate;
        [left, right] = [index * 2 + 1, index * 2 + 2];
      }
    }

    return min;
  }
  collect() {
    let results = [];
    while (this.store.length) {
      results.push(this.extract());
    }
    return results.reverse();
  }
}

const kClosest = (points, k) => {
  points = points.map((p) => {
    return {
      x: p[0],
      y: p[1],
      dist: Math.sqrt(Math.pow(p[0], 2) + Math.pow(p[1], 2)),
    };
  });

  let heap = new MaxHeap();

  for (const p of points) {
    heap.insert(p);

    if (heap.store.length > k) {
      heap.extract();
    }
  }

  return heap.collect().map((p) => [p.x, p.y]);
};

//let r = kClosest(
//  [
//    [1, 3],
//    [-2, 2],
//  ],
//  1
//);
//console.log(r);
// Input: points = [[1,3],[-2,2]], K = 1
// Output: [[-2,2]]
//let r = kClosest(
//  [
//    [3, 3],
//    [5, -1],
//    [-2, 4],
//  ],
//  2
//);
//console.log(r);
// Output: [[3,3],[-2,4]]

let r = kClosest(
  [
    [68, 97],
    [34, -84],
    [60, 100],
    [2, 31],
    [-27, -38],
    [-73, -74],
    [-55, -39],
    [62, 91],
    [62, 92],
    [-57, -67],
  ],
  5
);
console.log(r);
// [[2,31],[-27,-38],[-55,-39],[-57,-67],[34,-84]]
