#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 上午11:16
# @Title   : 167. 两数之和 II - 输入有序数组
# @Link    : https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/


QUESTION = """
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

示例:
输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
"""


THINKING = """
双指针，因为已经排好序了，所以从两端开始，比较两个指针对应的值的和sum和target的大小
如果小于target, 则左指针右移
如果大于target, 则右指针左移
如果相等，则返回索引(注意这里的索引是从1开始，所以各+1即可)
"""


from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while 1:
            s = numbers[i] + numbers[j]
            if s == target:
                return [i+1, j+1]
            if s < target:
                i += 1
            if s > target:
                j -= 1


if __name__ == '__main__':
    s = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    print(s.twoSum(numbers, target))
