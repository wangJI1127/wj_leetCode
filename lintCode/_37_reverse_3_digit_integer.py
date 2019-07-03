"""
你可以假设输入一定是一个只有三位数的整数，这个整数大于等于100，小于1000
样例
样例 1:

输入: number = 123
输出: 321

样例 2:

输入: number = 900
输出: 9
"""


class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """

    def reverseInteger(self, number):
        # write your code here
        return int(str(number)[::-1])

if __name__ == '__main__':
    sol = Solution()
    re = sol.reverseInteger(123)
    print(re)