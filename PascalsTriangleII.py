#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/12 下午3:12
# @Title   : 119. 杨辉三角 II
# @Link    : https://leetcode-cn.com/problems/pascals-triangle-ii/


QUESTION = """
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。


示例:
输入: 3
输出: [1,3,3,1]

进阶：
你可以优化你的算法到 O(k) 空间复杂度吗？
"""


THINKING = """
参考 118. 杨辉三角，其实是一道题，没啥算法在里面
"""


from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        result = [[1], [1, 1]]
        for i in range(2, rowIndex+1):
            current = [1]
            previous = result[i-1]
            pre_size = len(previous)
            for j in range(1, pre_size):
                current.append(previous[j] + previous[j-1])
            current.append(1)
            result.append(current)

        return result[-1]


if __name__ == '__main__':
    s = Solution()
    rowIndex = 3
    print(s.getRow(rowIndex))
