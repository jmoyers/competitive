/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} low
 * @param {number} high
 * @return {TreeNode}
 */
const trimBST = (root, low, high) => {
  const dfs = (node) => {
    if (!node) return null;
    node.left = dfs(node.left);
    node.right = dfs(node.right);

    if (node.val < low) {
      //console.log('node low, return right', node.val, node.right);
      return node.right;
    } else if (node.val > high) {
      //console.log('node high, return left', node.val, node.left);
      return node.left;
    } else {
      return node;
    }
  };

  return dfs(root);
};
