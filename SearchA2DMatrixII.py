#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 下午10:05
# @Title   : 240. 搜索二维矩阵 II
# @Link    : https://leetcode-cn.com/problems/search-a-2d-matrix-ii/


QUESTION = """
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target

该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。
"""


THINKING = """
从左下角开始找
如果大于target则向上找
如果小于target则向右找
如果越出边界，则返回False

思路就是一个点有4个方向，很难判定哪个方向是对的，想办法通过判断和target的大小关系，2个方向的去寻找
"""


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False

        x, y = len(matrix) - 1, 0
        max_x, max_y = len(matrix) - 1, len(matrix[0]) - 1

        while 1:
            current_number = matrix[x][y]
            if current_number < target:
                y += 1
            elif current_number > target:
                x -= 1
            else:
                result = True
                break
            if x < 0 or y > max_y:
                result = False
                break

        return result


if __name__ == '__main__':
    s = Solution()
    matrix = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target = 5
    print(s.searchMatrix(matrix, target))
