"""
给出 2 * n + 1个数字，除其中一个数字之外其他每个数字均出现两次，找到这个数字。

Example
样例 1:

输入：[1,1,2,2,3,4,4]
输出：3
解释：
仅3出现一次
样例 2:

输入：[0,0,1]
输出：1
解释：
仅1出现一次
Challenge
一次遍历，常数级的额外空间复杂度

Notice
n≤100
"""
class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        # write your code here
        for i in A:
            if A.count(i) == 1:
                return i
