#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/11 下午12:34
# @Title   : 416. 分割等和子集
# @Link    : https://leetcode-cn.com/problems/partition-equal-subset-sum/


QUESTION = """
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:
每个数组中的元素不会超过 100
数组的大小不会超过 200

示例 1:
输入: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成 [1, 5, 5] 和 [11].

示例 2:
输入: [1, 2, 3, 5]
输出: false
解释: 数组不能分割成两个元素和相等的子集.
"""


THINKING = """
1. 如果不能被2整除的话，肯定不能分成2个子集
2. 弄一个集合，记录遍历过程中所有遇到的数字组合的和
3. 如果能加到sum(nums) // 2，则表示能够分割成2个子集
"""


from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target, remain = divmod(sum(nums), 2)
        if remain:
            return False

        answer = {0}
        for i in nums:
            for j in list(answer):
                j += i
                if j == target:
                    return True
                answer.add(j)

        return False


if __name__ == '__main__':
    s = Solution()
    nums = [1, 5, 5, 11]
    print(s.canPartition(nums))
