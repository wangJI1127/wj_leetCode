"""
给定一个二叉树，找出其最小深度。

二叉树的最小深度为根节点到最近叶子节点的最短路径上的节点数量。

样例
样例 1:

输入: {}
输出: 0
样例 2:

输入:  {1,#,2,3}
输出: 3
解释:
	1
	 \
	  2
	 /
	3
它将被序列化为 {1,#,2,3}
样例 3:

输入:  {1,2,3,#,#,4,5}
输出: 2
解释:
      1
     / \
    2   3
       / \
      4   5
它将被序列化为 {1,2,3,#,#,4,5}
"""
"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        # write your code here
        if root == None:
            return 0
        return self.min_depth(root, 0)

    def min_depth(self, root, n):
        if root == None:
            return float("inf")
        if root.left == None and root.right == None:
            return n + 1
        return min(self.min_depth(root.left, n+1), self.min_depth(root.right, n+1))

