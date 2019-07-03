"""
两个排序的数组A和B分别含有m和n个数，找到两个排序数组的中位数，要求时间复杂度应为O(log (m+n))。

样例
样例1

输入:
A = [1,2,3,4,5,6]
B = [2,3,4,5]
输出: 3.5
样例2

输入:
A = [1,2,3]
B = [4,5]
输出: 3
挑战
时间复杂度为O(log n)
"""

class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):  # 暴力解法
        # write your code here
        A.extend(B)
        if len(A) & 1:
            return sorted(A)[len(A) // 2]
        else:
            return (sorted(A)[len(A) // 2] + sorted(A)[len(A) // 2 - 1]) / 2

    def findMedianSortedArrays1(self, A, B):
        pass

    def find(self, A, n1, B, n2):
        medA = n1 // 2
        medB = n2 // 2
        if n1 == 1:
            if n2 == 1:
                return (A[0] + B[0]) / 2
            elif n2 & 1:
                if A[0] == B[medB]:
                    return A[0]
                elif A[0] <= B[medB-1]:
                    return (B[medB-1] + B[medB]) / 2
                elif A[0] >= B[medB+1]:
                    return (B[medB] + B[medB+1]) / 2
                else:
                    return (B[medB] + A[0]) / 2
            else:
                if A[0] <= B[medB-1]:
                    return B[medB-1]
                elif A[0] >= B[medB]:
                    return B[medB]
                else:
                    return A[0]
        elif n2 == 1:
            if n1 & 1:
                if B[0] == A[medA]:
                    return B[0]
                elif B[0] <= A[medA-1]:
                    return (A[medA-1] + A[medA]) / 2
                elif B[0] >= A[medA+1]:
                    return (A[medA] + A[medA+1]) / 2
                else:
                    return (A[medA] + B[0]) / 2
            else:
                if B[0] <= A[medA-1]:
                    return A[medA-1]
                elif B[0] >= A[medA]:
                    return A[medA]
                else:
                    return B[0]
        else:
            cutlen = min(n1//2, n2//2)
            pass



if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6]
    B = [2, 3, 4, 5]
    so = Solution()


