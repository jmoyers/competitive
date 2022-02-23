/**
 * // Definition for a Node.
 * function Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {Node} node
 * @return {Node}
 */
const cloneGraph = (node) => {
  if (!node) return;
  const clones = {};
  const visited = new Set();

  const dfs = (curr) => {
    if (visited.has(curr.val)) return;
    visited.add(curr.val);

    let clone = clones[curr.val];
    if (clone) return clone;

    clone = new Node(curr.val);
    clones[curr.val] = clone;

    for (const n of curr.neighbors) {
      let neighbor = clones[n.val];

      if (neighbor) {
        clone.neighbors.push(neighbor);
      } else {
        clone.neighbors.push(dfs(n));
      }
    }

    return clone;
  };

  return dfs(node);
};
