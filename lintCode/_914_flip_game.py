"""
翻转游戏：给定一个只包含两种字符的字符串：+和-，你和你的小伙伴轮流翻转"++"变成"--"。当一个人无法采取行动时游戏结束，另一个人将是赢家。

编写一个函数，计算字符串在一次有效移动后的所有可能状态。

样例
样例1

输入: s = "++++"
输出:
[
  "--++",
  "+--+",
  "++--"
]
样例2

输入: s = "---+++-+++-+"
输出:
[
	"---+++-+---+",
	"---+++---+-+",
	"---+---+++-+",
	"-----+-+++-+"
]

"""
class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """
    def generatePossibleNextMoves(self, s):
        # write your code here
        res = list()
        for i in range(len(s) - 1):
            l = list(s)
            if s[i] == '+' and s[i] == s[i+1]:
                l[i] = '-'
                l[i+1] = '-'
                res.append(''.join(l))
        return res

if __name__ == '__main__':
    so = Solution()
    