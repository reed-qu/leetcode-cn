#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/17 下午3:30
# @Title   : 66. 加一
# @Link    : https://leetcode-cn.com/problems/plus-one/


QUESTION = """
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。

示例 2:
输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
"""


THINKING = """
首先对于Python来说实现还是很简单的，比如转化成数字之后，+1，然后放到列表里，但是效率差一些，其实这里主要就是考虑9的问题

从最后一位开始遍历，如果是9的话，则+1为0，继续往前找9，直到不是9的时候，+1就结束了，前面照写就行了

如果全是9，那也好办了，这是一种特殊情况，怎么处理都行，如果向上面那么处理之后第一位是0，那就再在第一位加个1
或者特殊处理，sum(digits) == 9 * len(digits)就直接返回[1] + [0] * len(digits)就行了
"""


from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        n = len(digits)
        for i in range(n-1, -1, -1):
            each = digits[i]
            if each == 9:
                result.insert(0, 0)
            else:
                result.insert(0, each+1)
                result = digits[:i] + result
                break
        if result[0] == 0:
            result.insert(0, 1)
        return result


if __name__ == '__main__':
    s = Solution()
    digits = [9, 9, 9, 9]
    print(s.plusOne(digits))
