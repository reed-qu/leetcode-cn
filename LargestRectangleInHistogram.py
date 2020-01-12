#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/12 下午3:46
# @Title   : 84. 柱状图中最大的矩形
# @Link    : https://leetcode-cn.com/problems/largest-rectangle-in-histogram/


QUESTION = """
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/histogram.png)
 
以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/histogram_area.png)

图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。


示例:
输入: [2,1,5,6,2,3]
输出: 10
"""


THINKING = """
维护一个栈，栈里记录的是：在单调递增的过程中，断掉的内个索引位置
为什么要找这个位置，是因为绘制矩形的时候，高度取决于最低的内个，类似于木桶理论
每次找到这个点时候，递增的开始到结束的区间内，遍历计算最大的面积，也就是一段一段的遍历计算
为了能肯定形成这个区间，要在数组的两端加上0
"""


from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        result = 0

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                result = max(result, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)

        return result


if __name__ == '__main__':
    s = Solution()
    heights = [2,1,5,6,2,3]
    print(s.largestRectangleArea(heights))
