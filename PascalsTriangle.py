#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/5 下午11:26
# @Title   : 118. 杨辉三角
# @Link    : https://leetcode-cn.com/problems/pascals-triangle/


QUESTION = """
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

![](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1],
[1,5,10,10,5,1]
]
"""


THINKING = """
无他，硬逻辑实现，时间复杂度O(N^2)
"""


from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        result = [[1], [1, 1]]
        for i in range(2, numRows):
            current = [1]
            previous = result[i-1]
            pre_size = len(previous)
            for j in range(1, pre_size):
                current.append(previous[j] + previous[j-1])
            current.append(1)
            result.append(current)

        return result


if __name__ == '__main__':
    s = Solution()
    numRows = 5
    print(s.generate(numRows))
