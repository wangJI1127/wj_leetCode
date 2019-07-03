"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):   # 暴力解法， 超出时间限制
            temp = numbers
            j = target - numbers[i]
            temp[i] = None
            if j in temp:
                return [i + 1, temp.index(j) + 1]

    def twoSum1(self, numbers, target):
        """
        解题思路： 类似于二分查找
            因为数组是有序的，所以先把数组的第一个数（最小）和最后一个数（最大）相加，然后与target比较，
            若target较小，则将right左移，减小total的值；若target较大，则将left右移，增大total的值。
        :param numbers:
        :param target:
        :return:
        """
        left = 0
        right = len(numbers) - 1
        total = numbers[left] + numbers[right]
        while(total != target):
            if(total > target):
                right -= 1
            elif total < target:
                left += 1
            total = numbers[left] + numbers[right]
        return [left+1, right+1]
