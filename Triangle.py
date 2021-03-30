#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2021/03/30 14:11:51
# @Title   : 120. 三角形最小路径和
# @Link    : https://leetcode-cn.com/problems/triangle/


QUESTION = """
给定一个三角形 triangle ，找出自顶向下的最小路径和。
每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。

示例 1：
输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
输出：11
解释：如下面简图所示：
   2
  3 4
 6 5 7
4 1 8 3
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

示例 2：
输入：triangle = [[-10]]
输出：-10
 
提示：
1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104

进阶：
你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题吗？
"""


THINKING = """
这个题的问题点主要是在不能每次找局部最优，应该遍历所有的路径，取全局最优
采用的方法是 自下而上 的方法
1. 最后一行为单个元素，所以从倒数第二行开始向上遍历
2. 
  6     5     7
 4 1   1 8   8 3
构成3个小三角形，每个小三角形的顶点都可以由下面2个数字，计算一个最小的和 [6, 5, 7] -> [7, 6, 10]
3. 一直向上计算，同时替换小三角形的顶点数字
4. 最后顶点的数字即为所求
"""


from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        l_total = len(triangle)
        for i in range(l_total-2, -1, -1):

            l_current = len(triangle[i])
            for j in range(l_current):

                triangle[i][j] += min(triangle[i+1][j:j+2])

        return triangle[0][0]


if __name__ == '__main__':
    tri = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    s = Solution()
    print(s.minimumTotal(tri))
