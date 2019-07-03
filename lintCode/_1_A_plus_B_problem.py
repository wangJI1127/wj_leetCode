"""
给出两个整数 aa 和 bb , 求他们的和。

样例
样例 1:

输入:  a = 1, b = 2
输出: 3
样例解释: 返回a+b的结果.
样例 2:

输入:  a = -1, b = 1
输出: 0
样例解释: 返回a+b的结果.
挑战
显然你可以直接 return a + b，但是你是否可以挑战一下不这样做？（不使用++等算数运算符）

说明
a和b都是 32位 整数么？

是的
我可以使用位运算符么？

当然可以
"""
"""
解题思路：在不使用“+”的情况下，只能使用位运算符，两个数相加的过程：
    1.先将两个数变为二进制
    2.然后对两个数进行位异或运算（^)
    3.然后两个数进行与运算（&），然后左移一位
    4.若第3步中，得到的结果为0，则位相加结果为2中得到的结果，否则，2,3两步的结果进行位相加即可得到结果
"""
class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        # write your code here
        return a + b

    def aplusb1(self, a, b):
        sum2 = a ^ b
        sum3 = (a & b) << 1
        # 以下可改为三元运算符
        # if(sum3 != 0):
        #     sum = self.aplusb1(sum2, sum3) # 递归  时间耗费较大
        # else:
        #     sum = sum2
        return sum2 if sum3 == 0 else self.aplusb1(sum2, sum3)

    def aplusb2(self, a, b):
        sum2 = a ^ b
        sum3 = (a & b) << 1
        while(sum3 != 0): # 迭代 时间耗费较大
            sum2 = a ^ b
            sum3 = (a & b) << 1
        return sum2

if __name__ == '__main__':
    so = Solution()
