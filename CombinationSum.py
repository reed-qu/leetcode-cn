#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/22 上午12:05
# @Title   : 39. 组合总和
# @Link    : https://leetcode-cn.com/problems/combination-sum/


QUESTION = """
给定一个无重复元素的数组 candidates 和一个目标数 target 
找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。

说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 

示例 1:
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]

示例 2:
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


THINKING = """
典型的回溯法问题，其实就是用递归，拆分成子问题，一层一层的递归解决
首先"解集不能包含重复的组合"，直接的思路就是排序，从小到大的寻找解集，不找比当前数字小的值，肯定就不会出现重复
其次的思想就是减法原则，target从解集中一个一个减下去，最后为0，反过来就是最后为0的这些解，就是正确解了
递归的停止条件也简单，当前的值比target大了的话就不用处理了，肯定不是正解，还有如果索引到最后一个值也就结束了
再次，这里允许重复的取数字，所以这里是一个交叉的写法
重复的话就继续取当前的数字，而tmp加上当前数字，target-当前数字
不重复的话则用当前的tmp和target继续往下一个数字寻找
"""


from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []

        n = len(candidates)
        result = []
        candidates.sort()

        def _dfs(i: int, tmp: List[int], target: int) -> None:
            if target == 0:
                result.append(tmp)
            if i == n  or target < candidates[i]:
                return
            _dfs(i, tmp+[candidates[i]], target - candidates[i])
            _dfs(i+1, tmp, target)

        _dfs(0, [], target)

        return result


if __name__ == '__main__':
    s = Solution()
    candidates = [2,3,6,7]
    target = 7
    print(s.combinationSum(candidates, target))
