#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/12 下午2:26
# @Title   : 77. 组合
# @Link    : https://leetcode-cn.com/problems/combinations/


QUESTION = """
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


THINKING = """
类似于 46. 全排列，也是用递归回溯的方法来实现，且要更简单一些
step从1开始，每深一层递归，都从step=i+1来构建下一个数
且重点是，每构建完1个组合之后，要把最后一个数字删除掉，来初始化，好进行下一次构建

用个大概的流程说明一下，更方便理解:

for i in range(1, 5):    # 表示1, 2, 3, 4
    current.append(i)    # current = [1]
    _dfs(i+1, current)   # _dfs(2, [1]) 到下一层递归中的去，这一层其实是有3个同级的
    
        _dfs(3, [1, 2])  # 触发return
        current.pop()    # current = [1]
        
        _dfs(4, [1, 3])  # 触发return
        current.pop()    # current = [1]
        
        _dfs(5, [1, 4])  # 触发return
        current.pop()    # current = [1]
        
    current.pop()        # current = []
"""


from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def _dfs(step: int, current: List) -> None:
            if len(current) == k:
                # 注意这里要复制出来一个副本[:]添加到result中
                # 否则的话，result中的结果会随着current改变而变
                result.append(current[:])
                return

            for i in range(step, n+1):
                current.append(i)
                _dfs(i+1, current)
                current.pop()

        _dfs(1, [])

        return result


if __name__ == '__main__':
    s = Solution()
    n = 4
    k = 2
    print(s.combine(n, k))
