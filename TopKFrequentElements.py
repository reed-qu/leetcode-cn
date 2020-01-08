#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 下午1:47
# @Title   : 347. 前 K 个高频元素
# @Link    : https://leetcode-cn.com/problems/top-k-frequent-elements/


QUESTION = """
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

示例 2:
输入: nums = [1], k = 1
输出: [1]

说明：
你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
"""


THINKING = """
1. 字典记录每个数字出现的次数
2. 转成[(), (), ..., ()]，然后制定key排序
3. 返回top_k
"""


from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for each in nums:
            if each not in count:
                count[each] = 1
            else:
                count[each] += 1

        top_k_items = list(count.items())
        top_k_items.sort(key=lambda x: x[1], reverse=True)
        return [top_k_items[i][0] for i in range(k)]


if __name__ == '__main__':
    s = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    print(s.topKFrequent(nums, k))
