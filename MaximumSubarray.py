#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/4 下午3:55
# @Title   : 53. 最大子序和
# @Link    : https://leetcode-cn.com/problems/maximum-subarray/


QUESTION = """
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6

解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

进阶:
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""


THINKING = """
用result记录不同序列和中最大一个，用total记录当前的序列最大和，然后遍历列表
total默认是列表中第一个值，所以列表从索引1开始遍历
如果total和当前数字和 total+nums[i] > 当前数字nums[i]，那么肯定是数字往大了走，total继续向后累加
否则total就放弃之前的序列，把当前的数字nums[i]作为total序列的起点，因为此时加上nums[i]还要<nums[i]，肯定是要舍弃的
前面的序列已经是局部最大的了，要看后面是否还存在更大的子序列
然后每次遍历完用max(total, result)记录一下全局最大值，直到遍历结束即可
"""


from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        total = nums[0]
        for i in range(1, len(nums)):
            if total + nums[i] > nums[i]:
            # if total > 0: 这样写也可以，但是不方便理解
                total += nums[i]
            else:
                total = nums[i]
            result = max(result, total)
        return result


if __name__ == '__main__':
    s = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(s.maxSubArray(nums))
