// A linked list is given such that each node contains an additional random
// pointer which could point to any node in the list or null.
// 
// Return a deep copy of the list.
// 
// The Linked List is represented in the input/output as a list of n nodes.
// Each node is represented as a pair of [val, random_index] where:
// 
//     val: an integer representing Node.val 
//
//     random_index: the index of the node (range from 0 to n-1) where random
//     pointer points to, or null if it does not point to any node.
// 
// Example 1:
// 
// Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
// Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
// 
// Example 2:
// 
// Input: head = [[1,1],[2,1]]
// Output: [[1,1],[2,1]]
// 
// Example 3:
// 
// Input: head = [[3,null],[3,0],[3,null]]
// Output: [[3,null],[3,0],[3,null]]
// 
// Example 4:
// 
// Input: head = []
// Output: []
// Explanation: Given linked list is empty (null pointer), so return null.
// 
// 
// Constraints:
// 
//     -10000 <= Node.val <= 10000
//     Node.random is null or pointing to a node in the linked list.
//     Number of Nodes will not exceed 1000.
class Node {
  constructor (val, next, random) {
    this.val = val;
    this.next = next;
    this.random = random;
  }
}

const copyRandomList = head => {
  let dummy = new Node();
  let curr = dummy;
  // since we're using objects as keys here and we cant get the actual
  // address of an object in javascript, we have to use a "Map" object
  // explcitly, which allows objects as keys
  const visited = new Map();

  const copyNode = node => {
    if (!node) return null;
    if (visited.has(node)) return visited.get(node);

    let n = new Node(node.val);

    // we set this early so that if we have a self referential loop
    // thru random, we can retrieve it during the node.random copy
    visited.set(node, n);

    n.random = node.random !== node ? copyNode(node.random, node) : n;

    return n;
  }

  while (head) {
    curr.next = copyNode(head);
    head = head.next;
    curr = curr.next;
  }

  return dummy.next;
}

// Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
// Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]


//console.log(copyRandomList(head));

const listFromArrWithRandom = list => {
  const refs = [];
  const randomLinks = [];

  let dummy = new Node();
  let curr = dummy;

  while (list.length) {
    const next = list.shift();
    curr.next = new Node(next[0]);
    refs.push(curr.next);
    if (next[1] !== null) {
      randomLinks.push([refs.length - 1, next[1]]);
    }
    curr = curr.next;
  }

  while (randomLinks.length) {
    const link = randomLinks.pop();
    refs[link[0]].random = refs[link[1]];
  }

  return refs[0];
}
// failing case
//    x      
// [[-1,4],[8,3],[7,null],[-3,null],[4,0]]

let head = listFromArrWithRandom([[-1,4],[8,3],[7,null],[-3,null],[4,0]]);

console.log(copyRandomList(head));

