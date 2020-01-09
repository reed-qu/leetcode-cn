#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 下午7:41
# @Title   : 72. 编辑距离
# @Link    : https://leetcode-cn.com/problems/edit-distance/


QUESTION = """
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

1. 插入一个字符
2. 删除一个字符
3. 替换一个字符

示例 1:
输入: word1 = "horse", word2 = "ros"
输出: 3
解释: 
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

示例 2:
输入: word1 = "intention", word2 = "execution"
输出: 5
解释: 
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
"""


THINKING = """
建议Google搜索，😝
有很多讲得很好的博客，比如：
https://www.dreamxu.com/books/dsa/dp/edit-distance.html
https://www.cnblogs.com/jiabei521/p/3353390.html
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        x, y = len(word1), len(word2)
        if not word1:
            return y
        if not word2:
            return x

        matrix = [[i] + [0] * y for i in range(x+1)]
        matrix[0] = list(range(y+1))

        for i in range(1, x+1):
            for j in range(1, y+1):
                alpha = 1
                if word1[i-1] == word2[j-1]:
                    alpha = 0

                matrix[i][j] = min([
                    matrix[i-1][j] + 1,
                    matrix[i][j-1] + 1,
                    matrix[i-1][j-1] + alpha
                ])

        return matrix[x][y]


if __name__ == '__main__':
    s = Solution()
    word1 = "intention"
    word2 = "execution"
    print(s.minDistance(word1, word2))
