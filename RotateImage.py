#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/24 下午3:54
# @Title   : 48. 旋转图像
# @Link    : https://leetcode-cn.com/problems/rotate-image/


QUESTION = """
给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。

说明：
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1:
给定 matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

示例 2:
给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""


THINKING = """
感觉像是个找规律题...

[                [                  [
   [1,2,3],         [1,4,7],           [7,4,1],
   [4,5,6],  ->     [2,5,8],   ->      [8,5,2],
   [7,8,9]          [3,6,9]            [9,6,3]
]                ]                  ]
            ↑                   ↑
           转置               依次倒序
"""


from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        matrix[:] = [x[::-1] for x in zip(*matrix)]


if __name__ == '__main__':
    s = Solution()
    matrix = [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ]
    print(s.rotate(matrix))
