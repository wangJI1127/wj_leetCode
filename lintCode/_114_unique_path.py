"""
有一个机器人的位于一个 m × n 个网格左上角。

机器人每一时刻只能向下或者向右移动一步。机器人试图达到网格的右下角。

问有多少条不同的路径？

样例
Example 1:

Input: n = 1, m = 3
Output: 1
Explanation: Only one path to target position.
Example 2:

Input:  n = 3, m = 3
Output: 6
Explanation:
	D : Down
	R : Right
	1) DDRR
	2) DRDR
	3) DRRD
	4) RRDD
	5) RDRD
	6) RDDR
注意事项
n和m均不超过100
"""
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        if(m == 1 or n == 1):
            return 1
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1) # 递归 时间复杂度大

    def uniquePaths1(self, m, n):
        if m == 0 or n == 0:
            return 0
        path = [[0 for i in range(n)] for i in range(m)] # n为列，m为行
        for i in range(m):
            path[i][0] = 1
        for i in range(n):
            path[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                path[i][j] = path[i-1][j] + path[i][j-1]
        return path[m-1][n-1]


if __name__ == '__main__':
       so = Solution()
