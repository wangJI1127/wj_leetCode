import _quick_sort
"""
给定一个未排序的整数数组，找到其中位数。

中位数是排序后数组的中间值，如果数组的个数是偶数个，则返回排序后数组的第N/2个数。

样例
样例 1:

输入：[4, 5, 1, 2, 3]
输出：3
解释：
经过排序，得到数组[1,2,3,4,5]，中间数字为3
样例 2:

输入：[7, 9, 4, 5]
输出：5
解释：
经过排序，得到数组[4,5,7,9]，第二个(4/2)数字为5
挑战
时间复杂度为O(n)

注意事项
数组大小不超过10000
"""
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the middle number of the array
    """
    def median(self, nums):
        # write your code here
        """
        使用python的话，直接使用sorted()函数排序就行
        :param nums:
        :return:
        """
        if(len(nums) % 2 == 0):
            med = len(nums) // 2
        else:
            med = len(nums) // 2 + 1
        return sorted(nums)[med - 1]

    def median1(self, nums):
        """
        若不使用python内置的排序函数，则需要自己编写排序函数，这里使用快速排序，
        :param nums:
        :return:
        """
        _quick_sort.QuickSort(nums, 0, len(nums) - 1)
        if (len(nums) % 2 == 0):
            med = len(nums) // 2
        else:
            med = len(nums) // 2 + 1
        return nums[med - 1]


if __name__ == '__main__':
    nums = [3, 4, 1, 2, 5]
    so = Solution()
