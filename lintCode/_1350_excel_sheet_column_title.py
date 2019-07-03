"""
给定一个正整数，返回相应的列标题，如Excel表中所示。

样例
样例1

输入: 28
输出: "AB"
样例2

输入: 29
输出: "AC"
注意事项
1 -> A
2 -> B
3 -> C
 ...
26 -> Z
27 -> AA
28 -> AB
"""

class Solution:
    """
    A 对应 65， Z 对应 90 , a 对应 97， z 对应 122。
    @param n: a integer
    @return: return a string
    """
    def convertToTitle(self, n):
        # write your code here
        return '' if n==0 else self.convertToTitle((n-1) // 26) + chr((n-1) % 26 + ord('A'))

if __name__ == '__main__':
    so = Solution()
