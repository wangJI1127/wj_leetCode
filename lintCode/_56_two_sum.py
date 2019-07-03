"""
给一个整数数组，找到两个数使得他们的和等于一个给定的数 target。

你需要实现的函数twoSum需要返回这两个数的下标, 并且第一个下标小于第二个下标。注意这里下标的范围是 0 到 n-1。

样例
Example1:
给出 numbers = [2, 7, 11, 15], target = 9, 返回 [0, 1].
Example2:
给出 numbers = [15, 2, 7, 11], target = 9, 返回 [1, 2].
挑战
Either of the following solutions are acceptable:

O(n) Space, O(nlogn) Time
O(n) Space, O(n) Time
注意事项
你可以假设只有一组答案。
"""
class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        for i in range(len(numbers)): # 暴力解法
            j = target - numbers[i]
            if (j in numbers and numbers.index(j) != i):
                return sorted([i, numbers.index(j)])