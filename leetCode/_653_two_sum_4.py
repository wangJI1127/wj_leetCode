"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True


Example 2:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):


    def findTarget(self, root, k):
        """
        解题思路：将二叉排序数转化为有序列表，然后类似于第1题和第167题。
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        l = list()
        self.tree2list(root, l)
        for i in range(len(l)): # 暴力解法 速度较慢
            j = k - l[i]
            if (j in l and l.index(j) != i):
                return [i, l.index(j)]
    def tree2list(self, root, l):
        if root==None:
            return
        l.append(root.val)
        self.tree2list(root.left, l)
        self.tree2list(root.right, l)


    def findTarget1(self, root, k):
        """
        解题思路： 先将根节点数值放入集合s中，判断集合中是否有对应的另一个数值。
            然后查找根节点的左子树和右子树， 以此遍历二叉树。
            此方法，集合s是一个全局变量，会包含某一节点以前的所有节点
        :param root:
        :param k:
        :return:
        """
        s = set()
        return self.find(root, k, s)
    def find(self, root, k, s):
        if root==None:
            return False
        if (k - root.val) in s:
            return True
        s.add(root.val)
        return self.find(root.left, k, s) or self.find(root.right, k, s)

