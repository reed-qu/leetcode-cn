#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/25 下午3:16
# @Title   : 55. 跳跃游戏
# @Link    : https://leetcode-cn.com/problems/jump-game/


QUESTION = """
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。

示例 1:
输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。

示例 2:
输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0，所以你永远不可能到达最后一个位置。
"""


THINKING = """
这个问题有一个小技巧，不太容易找出来，根据就是只要能到达某一索引x处，那么就x之前所有的索引处都是能到达的
举几个例子就好理解一些，这里数组里的数字表示该位置的最大跳跃长度，也就是说跳出数组了并没有问题
只要看最远能到达的位置>=最后一位，即表示可以到达最后一位
所以我们在遍历数组的时候，目标就是找能调到最远距离的内个索引
遍历中每一次需要做比较就是看 如果从当前位置起跳 和 最远的距离 二者谁更远一些，也就是max(i+nums[i], current_index)

比如数组是[3, 1, 0, 2, 6, 0, 1, 1, 3, 4]
1. current_index = 0, i = 0, 0+nums[0] = 3, 最远距离是3
2. current_index = 3, i = 1, 1+nums[1] = 2, 最远距离还是3，此时不需要先跳到2，再到3了
3. current_index = 3, i = 2, 2+nums[2] = 2, 同上
4. current_index = 3, i = 3, 3+nums[3] = 5, 最远距离是5，如果所有的最远距离都只能到达这里的话，那么就是死局了，因为这里能跳的只是0
5. current_index = 5, i = 4, 4+nums[4] = 10, 可见从此处跳的话，最远能跳到10的位置，也就舍掉第"4"步，也就是从数字2跳到数字6，只1步
然后从数字6跳可以跳到索引10的位置，显然更远，也到了最后了
如果这里的6改成1的话，就会继续往后遍历，遍历到索引6的时候，就会发现，最远距离在当前索引之前了，就表示已经死局了，返回False 
"""


from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current_index = 0
        size = len(nums)
        for i in range(size):
            if i > current_index:
                return False
            current_index = max(i+nums[i], current_index)
            if current_index >= size - 1:
                return True


if __name__ == '__main__':
    s = Solution()
    nums = [3, 1, 0, 2, 6, 0, 1, 1, 3, 4]
    print(s.canJump(nums))
