#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/30 下午9:35
# @Title   : 121. 买卖股票的最佳时机
# @Link    : https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/


QUESTION = """
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润
注意你不能在买入股票前卖出股票。

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""


THINKING = """
本质是从列表里面，找出两个极值，然后有个条件就是index_max > index_min

引入两个变量，分别记录最大值和最小值，max_, min_
最大值初始化为0，会逐步的找到更大的值，否则的话就像示例2一样，返回这个初始化的值0
最小值初始化为prices[0]，然后从列表第一位开始比较max_和新的prices[i] - min_，然后把更大的更新给max_，留给下次迭代用
然后再比较min_和prices[i]，更新最小值，也是留给下次迭代用
这样如果在前面找到了全局最小值，那么min_就再也不会更新，只要在后面找到最大的max_就可以了
"""


from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        if l <= 1:
            return 0

        max_ = 0
        min_ = prices[0]
        for i in range(1, l):
            max_ = max(max_, prices[i] - min_)
            min_ = min(min_, prices[i])
        return max_


if __name__ == '__main__':
    s = Solution()
    prices = [7,1,5,3,6,4]
    print(s.maxProfit(prices))
