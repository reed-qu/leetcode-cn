#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/15 下午11:05
# @Title   : 11. 盛最多水的容器
# @Link    : https://leetcode-cn.com/problems/container-with-most-water/


QUESTION = """
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
图片链接: https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/07/25/question_11.jpg

示例:
输入: [1,8,6,2,5,4,8,3,7]
输出: 49
"""


THINKING = """
根据题设可以得知，输出的面积就是列表中的某2个角标i, j差与i, j中小的内个值的乘积(类似于木桶理论，主要取决于短板)
暴力方法当然可行，但是效率太差，2个角标自然思路就是双指针，初始化i, j = 0, len(height)-1
然后二者往中间移动，当移动到同一点的时候，二者之间间隔为0即停止，期间记录最大的乘积，最后返回即可

但是这里面有个问题就是i, j如何移动？所谓的面积的计算公式其实是这样的: (j - i) * min(height[i], height[j])
那么此时如果i 或者 j移动一个单位，那么(j - i)肯定是减少1的，height[i], height[j]其中的大的内个
那么移动之后，要么比小的内个还小，要么min(height[i], height[j])还是等于小的内个，总之面积肯定是减少的，这种情况没必要选择

而如果移动小的内个，(j - i)虽然还是会变小，但是min(height[i], height[j])有可能变大，面积是可能变大的
所以这个动作是有必要的，所以这里只需要移动height[i], height[j] 大的内个就可以了
"""


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_ = 0
        i, j = 0, len(height)-1
        while i < j:
            left, right = height[i], height[j]
            area = (j - i) * min(left, right)
            max_ = max(max_, area)
            if left < right:
                i += 1
            else:
                j -= 1
        return max_


if __name__ == '__main__':
    s = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(s.maxArea(height))
