/**
 * // Definition for a Node.
 * function Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {Node} head
 * @return {Node}
 */
var copyRandomList = function (head) {
  // create a memoized copy node function
  // it calls itself recursively for random and next

  const store = {};
  let id = 0;

  const copyNode = (node) => {
    if (!node) return node;
    if (node.id) {
      return store[node.id];
    } else {
      const clone = new Node(node.val);

      node.id = ++id;
      store[node.id] = clone;

      clone.random = copyNode(node.random);
      clone.next = copyNode(node.next);
      return clone;
    }
  };

  return copyNode(head);
};
