// There is a new alien language which uses the latin alphabet. However, the
// order among letters are unknown to you. You receive a list of non-empty words
// from the dictionary, where words are sorted lexicographically by the rules of
// this new language. Derive the order of letters in this language.
//
// Input:
// [
//   "wrt",
//   "wrf",
//   "er",
//   "ett",
//   "rftt"
// ]
//
// Output: "wertf"
//
// Example 2:
//
// Input:
// [
//   "z",
//   "x"
// ]
//
// Output: "zx"
//
// Example 3:
//
// Input:
// [
//   "z",
//   "x",
//   "z"
// ]
//
// Output: ""
//
// Explanation: The order is invalid, so return "".
//
// Note:
//
//     You may assume all letters are in lowercase.
//     If the order is invalid, return an empty string.
//     There may be multiple valid order of letters

class Graph {
  constructor() {
    this.adjacency = {};
    this.invalid = false;
  }
  addEdge(a, b) {
    this.adjacency[a] = this.adjacency[a] || [];
    if (a === b) return;
    if (!this.adjacency[a].includes(b)) this.adjacency[a].push(b);
  }
  topologicalSort() {
    const visited = {};
    const grey = {};
    const stack = [];

    // perform a depth first search from any point
    const dfs = (node) => {
      // if we are currently already exploring node,
      // we've detected a cycle. in lexographic terms, this means the whole
      // input set is invalid
      if (grey[node]) this.invalid = true;
      else grey[node] = true;

      if (visited[node]) {
        grey[node] = false;
        return;
      }

      visited[node] = true;

      const children = this.adjacency[node] || [];

      for (const child of children) {
        dfs(child);
      }

      grey[node] = false;

      stack.push(node);
    };

    for (let letter in this.adjacency) {
      // lazy mans way of making sure we hit them all
      dfs(letter);
    }

    return this.invalid ? [] : stack;
  }
}

const alienOrder = (words) => {
  // the structure we use is a graph with edges that represent
  // direcitonal order between individual letters.
  // letters are the vertexes in this case.
  // edges
  // - 1st letter of each word
  // - where an identical prefix between subsequent words is detected
  //   we can infer order of the letters where the prefix deviates.
  //   an example is "bfe" > "bfc" -- in this case c would come after e
  //   in the lexographic sort
  // after we build this graph, we can use a topological sort to build a
  // lexograph, with some ambiguity where the edges don't provide 100%
  // specificity on order

  const lexoGraph = new Graph();

  let lastWord = false;

  for (const word of words) {
    // add at a minimum an empty vertex
    for (const char of word) {
      lexoGraph.addEdge(char, char);
    }

    if (lastWord) {
      let i = 0;
      let couldBePrefix = true;

      while (i < word.length && i < lastWord.length && couldBePrefix) {
        if (word[i] !== lastWord[i]) {
          couldBePrefix = false;
          lexoGraph.addEdge(lastWord[i], word[i]);
        } else {
          lexoGraph.addEdge(word[i], word[i]);
        }

        i++;
      }

      if (couldBePrefix && lastWord.length > word.length) {
        lexoGraph.invalid = true;
      } else if (couldBePrefix) {
        lexoGraph.addEdge(lastWord[lastWord.length - 1], word[word.length - 1]);
      }
    }
    lastWord = word;
  }

  return lexoGraph.topologicalSort().reverse().join("");
};

const res = alienOrder(["wrt", "wrf", "er", "ett", "rftt"]);

//const res = alienOrder(["ac", "ab", "b"]);
// const res = alienOrder(["abc", "ab"]);

// const res = alienOrder([
//   "bsusz",
//   "rhn",
//   "gfbrwec",
//   "kuw",
//   "qvpxbexnhx",
//   "gnp",
//   "laxutz",
//   "qzxccww",
// ]);

console.log(res);
