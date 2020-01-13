#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/13 上午10:35
# @Title   : 404. 左叶子之和
# @Link    : https://leetcode-cn.com/problems/sum-of-left-leaves/


QUESTION = r"""
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
"""


THINKING = """
递归，所有左子树的和，并不代表只往左走，所以还是要遍历整棵树，把左子树求和
递归中标记is_left: 是否是左子树，控制是要累加当前这个值
其他的没什么可说的了，二叉树中递归是最常见的了
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.number = 0

        def _calc_sum(node: TreeNode, is_left=False) -> None:
            if not node.left and not node.right and is_left:
                self.number += node.val
                return

            if node.left:
                _calc_sum(node.left, is_left=True)
            if node.right:
                _calc_sum(node.right, is_left=False)

        _calc_sum(root)

        return self.number


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    left = TreeNode(9)
    right = TreeNode(20)
    right_left = TreeNode(15)
    right_right = TreeNode(7)
    right.left = right_left
    right.right = right_right
    root.left = left
    root.right = right
    print(s.sumOfLeftLeaves(root))
