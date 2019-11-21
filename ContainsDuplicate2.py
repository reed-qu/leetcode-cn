#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 上午11:55
# @Title   : 219. 存在重复元素 II
# @Link    : https://leetcode-cn.com/problems/contains-duplicate-ii/


QUESTION = """
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j
使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:
输入: nums = [1,2,3,1], k = 3
输出: true

示例 2:
输入: nums = [1,0,1,1], k = 1
输出: true

示例 3:
输入: nums = [1,2,3,1,2,3], k = 2
输出: false
"""


THINKING = """
借助哈希表来实现，从列表的开头开始遍历
如果哈希表中不存在，则创建key: nums[i]; value: i
如果存在则要计算二者的索引查 delta
    如果delta <= k，那么返回True
    否则的话，更新key的值为新的i
然后继续遍历，如果到最后也没有遇到True的话，即返回False
"""


from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        record = {}
        l = len(nums)
        for i in range(l):
            if nums[i] not in record:
                record[nums[i]] = i
            else:
                if i - record[nums[i]] <= k:
                    return True
                else:
                    record[nums[i]] = i
        return False


if __name__ == '__main__':
    s = Solution()
    nums = [1, 0, 1, 1]
    k = 1
    print(s.containsNearbyDuplicate(nums, k))
