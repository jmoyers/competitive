// Given a non-empty list of words, return the k most frequent elements.
//
// Your answer should be sorted by frequency from highest to lowest. If two
// words have the same frequency, then the word with the lower alphabetical
// order comes first.
//
// Example 1:
//
// Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
// Output: ["i", "love"]
// Explanation: "i" and "love" are the two most frequent words.
//     Note that "i" comes before "love" due to a lower alphabetical order.
//
// Example 2:
//
// Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is",
// "is"], k = 4
// Output: ["the", "is", "sunny", "day"]
// Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
// with the number of occurrence being 4, 3, 2 and 1 respectively.
//
// Note:
//
//     You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
//     Input words contain only lowercase letters.
//
// Follow up:
//
//     Try to solve it in O(n log k) time and O(n) extra space.

class MinHeap {
  constructor() {
    this.store = [];
    this.comparator = (a, b) => {
      if (typeof b === "undefined") return false;
      if (a.freq === b.freq) return a.word < b.word;
      return a.freq > b.freq;
    };
  }

  insert(word, freq) {
    if (this.store.length === 0) this.store.push({ word, freq });
    else {
      this.store.push({ word, freq });

      let index = this.store.length - 1;
      let parent = Math.floor((index - 1) / 2);

      while (
        this.store[parent] &&
        this.comparator(this.store[parent], this.store[index])
      ) {
        this.swap(index, parent);
        index = parent;
        parent = Math.floor((index - 1) / 2);
      }
    }
  }

  swap(i, j) {
    let tmp = this.store[i];
    this.store[i] = this.store[j];
    this.store[j] = tmp;
  }

  extract() {
    if (this.store.length === 0) return false;

    this.swap(0, this.store.length - 1);

    let min = this.store.pop();

    let index = 0;
    let [left, right] = [index * 2 + 1, index * 2 + 2];
    let shouldSwap = true;

    // swap the root with its lower child all the way down
    while (shouldSwap && left < this.store.length) {
      // if the left child exists and is lower than right child
      let isLeftCandidate = !this.comparator(
        this.store[left],
        this.store[right]
      );

      let swapCandidate = isLeftCandidate ? left : right;

      shouldSwap = this.comparator(
        this.store[index],
        this.store[swapCandidate]
      );

      if (shouldSwap) {
        this.swap(index, swapCandidate);
        index = swapCandidate;
        [left, right] = [index * 2 + 1, index * 2 + 2];
      }
    }

    return min;
  }

  getK(k) {
    let result = [];
    for (let i = 0; i < k; i++) {
      let record = this.extract();
      result.push(record.word);
    }
    return result;
  }
}

const topKFrequent = (words, k) => {
  // first count frequency of words using a single loop and a map
  // next add the words to a max heap that stores k elements
  // you could just have a non-limited heap, but in cases where the number
  // of words are very large, you end up having an increased insertion and
  // removal time. in the worst case (where n = no of words, and k = no of
  // words) this would be the same, but intuitively k is likely to be smaller
  // than n most of the time

  // count words
  const wordMap = {};

  for (const word of words) {
    wordMap[word] = wordMap[word] ? wordMap[word] + 1 : 1;
  }

  let heap = new MinHeap();
  for (const w in wordMap) {
    heap.insert(w, wordMap[w]);

    if (heap.store.length > k) {
      heap.extract();
    }
  }

  return heap.getK(k).reverse();
};

//let r = topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2);
//Output: ["i", "love"]
//let r = topKFrequent(
//  ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
//  4
//);
//Output: ["the", "is", "sunny", "day"]

let r = topKFrequent(["aaa", "aa", "a"], 2);
