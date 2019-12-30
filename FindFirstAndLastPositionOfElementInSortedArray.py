#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 下午10:46
# @Title   : 34. 在排序数组中查找元素的第一个和最后一个位置
# @Link    : https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/


QUESTION = """
给定一个按照升序排列的整数数组 nums，和一个目标值 target
找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
"""


THINKING = """
特殊的二分查找算法
思路是先找左索引，再找右索引，有一点不同则是需要加一点变化
找左右索引的时候引入一个hit_left的变量，表示是否要命中最小的内个左索引
同时要判断mid的值是否等于target，如果相等的话其实还没完，因为不一定是最小或者最大的内个
知道找到最小或者最大的内个才结束
同时注意特殊的地方，在找最大的索引的时候，因为返回的left = mid + 1，而mid是target
所以要减1
"""


from typing import List


class Solution:
    def _binary_search(self, nums: List[int], target: int, hit_left: bool) -> int:
        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right - left) // 2
            # 在找left_idx的时候实际是nums[mid] >= target
            # 在招right_index的时候实际是nums[mid] > target
            # 用hit_left这个bool在控制
            if nums[mid] > target or (hit_left and target == nums[mid]):
                right = mid
            else:
                left = mid + 1

        return left


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_idx = self._binary_search(nums, target, True)
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]
        right_idx = self._binary_search(nums, target, False) - 1

        return [left_idx, right_idx]


if __name__ == '__main__':
    s = Solution()
    nums = [5,7,7,8,10]
    target = 8
    print(s.searchRange(nums, target))
