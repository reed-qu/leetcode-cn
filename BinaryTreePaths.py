#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/12 上午10:52
# @Title   : 257. 二叉树的所有路径
# @Link    : https://leetcode-cn.com/problems/binary-tree-paths/


QUESTION = r"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
"""


THINKING = """
二叉树最典型的解法就是递归
主要是_find_path的递归写法，分3种情况
1. 往左节点走
2. 往右节点走
3. 左右节点都是None，即走到头了

首先在每层递归中，要把当前的node.val添加到临时列表中pre_path
这样在找到第3中情况的时候，就可以往result添加一条路径，且返回，
这里向上一层返回的时候要注意，返回一层要把pre_path中的最后一个pop掉，这样才能继续正常递归
"""


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        result = []

        def _find_path(node, pre_path):
            pre_path.append(str(node.val))
            if not node.left and not node.right:
                result.append("->".join(pre_path))
                return
            if node.left:
                _find_path(node.left, pre_path)
                pre_path.pop()
            if node.right:
                _find_path(node.right, pre_path)
                pre_path.pop()

        _find_path(root, [])

        return result


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    left_right = TreeNode(5)
    left.right = left_right
    root.left = left
    root.right = right
    print(s.binaryTreePaths(root))
