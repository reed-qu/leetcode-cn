#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/3 下午3:41
# @Title   : 287. 寻找重复数
# @Link    : https://leetcode-cn.com/problems/find-the-duplicate-number/


QUESTION = """
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:
输入: [1,3,4,2,2]
输出: 2

示例 2:
输入: [3,1,3,4,2]
输出: 3

说明：
    不能更改原数组（假设数组是只读的）。
    只能使用额外的 O(1) 的空间。
    时间复杂度小于 O(n^2) 。
    数组中只有一个重复的数字，但它可能不止重复出现一次。
"""


THINKING = """
解法1: findDuplicate2
    思路很直接，先排序，然后从头往后找，如果前后两个一致的话，那就返回
    这没什么可说的，复杂度上也是可行的，但是如果这样的话就算不上什么算法了
    
解法2: findDuplicate
    题设有个很重要的前提，就是数字都是在1-n之间的，所以真正想表达的是"值作为索引不会越界"
    而且其中肯定是有重复的值的，这里的特点不明显，仔细思考或者假设一下就会发现
    如果把值作为下一次的索引来找的话，就是一个"有环链表"，所以采用同样的快慢指针的套路来找到环路开始的位置
    
    然后设置两个步长=1的指针，一个从头走，一个在循环里走，这样的话，肯定会碰上，碰上的时候就是返回值
"""


from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        index1 = 0
        index2 = slow
        while index1 != index2:
            index1 = nums[index1]
            index2 = nums[index2]

        return index1


    def findDuplicate2(self, nums: List[int]) -> int:
        nums.sort()
        size = len(nums)
        for i in range(size-1):
            if nums[i] == nums[i+1]:

                return nums[i]


if __name__ == '__main__':
    s = Solution()
    inde = [0,1,2,3,4]
    nums = [1,3,4,2,2]
    print(s.findDuplicate(nums))
