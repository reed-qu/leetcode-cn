#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 上午10:35
# @Title   : 560. 和为K的子数组
# @Link    : https://leetcode-cn.com/problems/subarray-sum-equals-k/


QUESTION = """
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :
输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。

说明 :
数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
"""


THINKING = """
思路就是如果暴力穷举肯定时间复杂度太高，怎么能尽量将时间复杂度控制在O(n)，也就是遍历一次
一般这种情况为了记录前面的状态，要引入哈希表，用空间来换时间

哈希表中存的是从前往后遍历的和对应出现的次数，如果不存在则初始化为1，如果存在则+=1
同时这里要关注累加的和total_sum-k的值，如果这个值存在于哈希表中
代表当前这个值 等于前面的出现过的某个子序列，这样就肯定会再形成1个解
问题可解
"""


from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_count = {0: 1}
        count = 0
        total_sum = 0

        for each in nums:
            total_sum += each
            sub_sum = total_sum - k

            if sub_sum in sum_count:
                count += sum_count[sub_sum]
            sum_count[total_sum] = sum_count.get(total_sum, 0) + 1

        return count


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 1, 2, 1]
    k = 3
    print(s.subarraySum(nums, k))
