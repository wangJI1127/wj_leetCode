"""
线段树是一棵二叉树，他的每个节点包含了两个额外的属性start和end用于表示该节点所代表的区间。start和end都是整数，并按照如下的方式赋值:

根节点的 start 和 end 由 build 方法所给出。
对于节点 A 的左儿子，有 start=A.left, end=(A.left + A.right) / 2。
对于节点 A 的右儿子，有 start=(A.left + A.right) / 2 + 1, end=A.right。
如果 start 等于 end, 那么该节点是叶子节点，不再有左右儿子。
实现一个 build 方法，接受 start 和 end 作为参数, 然后构造一个代表区间 [start, end] 的线段树，返回这棵线段树的根。

Example
样例 1:

输入：[1,4]
输出："[1,4][1,2][3,4][1,1][2,2][3,3][4,4]"
解释：
	               [1,  4]
	             /        \
	      [1,  2]           [3, 4]
	      /     \           /     \
	   [1, 1]  [2, 2]     [3, 3]  [4, 4]
样例 2:

输入：[1,6]
输出："[1,6][1,3][4,6][1,2][3,3][4,5][6,6][1,1][2,2][4,4][5,5]"
解释：
	       [1,  6]
             /        \
      [1,  3]           [4,  6]
      /     \           /     \
   [1, 2]  [3,3]     [4, 5]   [6,6]
   /    \           /     \
[1,1]   [2,2]     [4,4]   [5,5]
Clarification
线段树(又称区间树), 是一种高级数据结构，他可以支持这样的一些操作:

查找给定的点包含在了哪些区间内
查找给定的区间包含了哪些点
"""
"""
Definition of SegmentTreeNode:

"""
class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None

class Solution:
    """
    @param: start: start value.
    @param: end: end value.
    @return: The root of Segment Tree.
    """
    def build(self, start, end):
        # write your code here
        # 层次遍历 该方法时间复杂度较高
        if(start > end):
            return None
        if(start == end):
            return SegmentTreeNode(start, end)
        queue = list()
        sement = SegmentTreeNode(start, end)
        queue.append(sement)
        while(len(queue) != 0):
            temp = queue.pop(0)
            if(temp.start != temp.end):
                left = SegmentTreeNode(temp.start, (temp.start+temp.end)//2)
                right = SegmentTreeNode((temp.start+temp.end)//2+1, temp.end)
                queue.append(left)
                queue.append(right)
                temp.left = left
                temp.right = right
        return sement

    def build1(self, start, end):
        # 分治法
        if (start > end):
            return None
        if (start == end):
            return SegmentTreeNode(start, end)
        sement = SegmentTreeNode(start, end)
        sement.left = self.build1(start, (start+end)//2)
        sement.right = self.build1((start+end)//2+1, end)
        return sement


if __name__ == '__main__':
    sol = Solution()
    re = sol.build(1,4)
