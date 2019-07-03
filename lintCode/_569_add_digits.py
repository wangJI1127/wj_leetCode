"""
给出一个非负整数 num，反复的将所有位上的数字相加，直到得到一个一位的整数。

Example
例1:

输入:
num=38
输出:
2
解释:
过程如下： 3 + 8 = 11, 1 + 1 = 2. 因为 2 只有一个数字，返回 2.

例2:

输入:
num=9
输出:
9
解释:
9<10,返回 9.
Challenge
你可以不用任何的循环或者递归算法，在 O(1) 的时间内解决这个问题么？
"""

class Solution:
    """
    @param num: a non-negative integer
    @return: one digit
    """
    """
        主要在于找规律
        解题思路：任何数各位反复相加，最终得到一个个位数：若该数是9的倍数，则结果必为9，否则结果为该数的各个数位相加后对9取余。
    """

    def addDigits(self, num):
        # write your code here
        if num % 9 == 0:
            return 9
        else:
            sum = 0
            while(num != 0): # 循环
                sum = sum + num % 10
                num = num // 10
            return sum % 9

    def addDigits1(self, num):
        if num <= 9:
            return num
        return self.addDigits1(num // 10 + num % 10) # 递归

    def addDigits2(self, num):
        return 0 if num == 0 else (num - 1) % 9 + 1

if __name__ == '__main__':
    so = Solution()
    s = so.addDigits(384)
    s1 = so.addDigits1(384)
    s2 = so.addDigits2(384)