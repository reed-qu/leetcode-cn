#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/7 上午10:05
# @Title   : 64. 最小路径和
# @Link    : https://leetcode-cn.com/problems/minimum-path-sum/


QUESTION = """
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""


THINKING = """
有些类似 62. 不同路径 | #6
规定只能往右和往下走，是一个动态规划问题
要想走到某一个点x的最短路径和，等于min(x上面的点的最短路径, x左边的点的最短路径) + 当前x所在位置的值

1 3 1        1     1+3=4     4+1=5
1 5 1  ->  1+1=2 min(4,2)+5   ...
4 2 1      2+4=6    ...       ...

有了这个状态转移方程，就一切都好办了，只不过为了避免索引溢出，需要考虑在边界上的情况
只要考虑第一行和第一列这两个边界就可以了，往右和往下我们有限制，肯定不会溢出
1. 第一行的情况，只和前面的数字累加
2. 第一列的情况，只和上面的数字累加
3. 如果不在边界上，则按照上面的状态转移方程在原数组上，重新构建出一个累加的数组
右下角的数字即是最小的路径和
"""


from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        for i in range(row):
            for j in range(col):
                if i > 0 and j > 0:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
                elif i == 0 and j > 0:
                    grid[i][j] = grid[i][j] + grid[i][j-1]
                elif i > 0 and j == 0:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                else:
                    pass

        return grid[row-1][col-1]


if __name__ == '__main__':
    s = Solution()
    grid = [
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]
    print(s.minPathSum(grid))
