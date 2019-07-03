import heapq
"""
数字是不断进入数组的，在每次添加一个新的数进入数组的同时返回当前新数组的中位数。

样例
样例1

输入: [1,2,3,4,5]
输出: [1,1,2,2,3]
样例说明：
[1] 和 [1,2] 的中位数是 1.
[1,2,3] 和 [1,2,3,4] 的中位数是 2.
[1,2,3,4,5] 的中位数是 3.
样例2

输入: [4,5,1,3,2,6,0]
输出: [4,4,4,3,3,3,3]
样例说明：
[4], [4,5] 和 [4,5,1] 的中位数是 4.
[4,5,1,3], [4,5,1,3,2], [4,5,1,3,2,6] 和 [4,5,1,3,2,6,0] 的中位数是 3.
挑战
时间复杂度为O(nlogn)

说明
中位数的定义：

这里的中位数不等同于数学定义里的中位数。
中位数是排序后数组的中间值，如果有数组中有n个数，则中位数为A[(n-1)/2]A[(n−1)/2]。
比如：数组A=[1,2,3]的中位数是2，数组A=[1,19]的中位数是1。

讲解： https://blog.csdn.net/qq_33575542/article/details/80881015
"""
class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        # write your code here
        l = list()
        for i in range(len(nums)):
            l.append(self.median(nums, 0, i+1)) # 此方法耗费时间太久
        return l

    def median(self, nums, start, end):
        # 此方法是80题的方法
        temp = nums[start:end]
        if (len(temp) % 2 == 0):
            med = len(temp) // 2
        else:
            med = len(temp) // 2 + 1
        return sorted(temp)[med - 1]


    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def insertHeap(self, num):
        if (len(self.minHeap) + len(self.maxHeap)) & 1: # 如果为奇数， 插入最大堆
            if len(self.minHeap) > 0:
                if num > self.minHeap[0]:  # 大于最小堆里的最小元素
                    heapq.heappush(self.minHeap, num)  # 新数据先插入最小堆
                    heapq.heappush(self.maxHeap, -self.minHeap[0])  # 最小堆中的最小元素插入最大堆
                    heapq.heappop(self.minHeap) # 删除刚刚插入到最大堆中的元素
                else:
                    heapq.heappush(self.maxHeap, -num)
            else:
                heapq.heappush(self.maxHeap, -num)
        else: # 为偶数， 插入最小堆
            if len(self.maxHeap) > 0:
                if num < -self.maxHeap[0]:  # 小于最大堆里的最大元素
                    heapq.heappush(self.maxHeap, -num)  # 新数据先插入最大堆
                    heapq.heappush(self.minHeap, -self.maxHeap[0])  # 最大堆中的最大元素插入最小堆
                    heapq.heappop(self.maxHeap)
                else:
                    heapq.heappush(self.minHeap, num)
            else:
                heapq.heappush(self.minHeap, num)

    def getMedian(self, n=None):
        if (len(self.maxHeap) + len(self.minHeap)) & 1: # 先插入的最小堆
            mid = self.minHeap[0]
        else:
            mid = -self.maxHeap[0]
        return mid

    def medianII1(self, nums):
        """
        如[1,2,3,4,5]， 最终结果：[1,2]为最大堆，[3,4,5]为最小堆。
        用两个堆保存数据，保证两个堆的数据保持平衡（元素个数相差不超过1）大顶堆存放的数据要比小顶堆的数据小,
        如果两个堆中的元素数量为奇数，则将新元素插入最大堆；如果要加入的数据，比小顶堆的最小元素大，先将该元素插入小顶堆，
        然后将小顶堆的最小元素插入到大顶堆。
        如果两个堆中的元素数量为偶数，则将新元素插入最小堆；如果要加入的数据，比大顶堆的最大元素小，先将该元素插入大顶堆，
        然后将大顶堆的最大元素插入到小顶堆。
        :param nums:
        :return:
        """
        l = list()
        for i in range(len(nums)):
            self.insertHeap(nums[i])
            l.append(self.getMedian())
        return l



if __name__ == '__main__':
    l = [4,5,1,3,2,6,0]
    so = Solution()