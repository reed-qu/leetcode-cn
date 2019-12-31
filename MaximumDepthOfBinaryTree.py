#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/30 下午9:07
# @Title   : 104. 二叉树的最大深度
# @Link    : https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/


QUESTION = """
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数
说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
"""


THINKING = """
递归查找

如果当前节点是None, 那么返回0
否则的话，分别考虑左右两个子树，搜索左右两个子树的深度
直到搜索到None, 那么这个节点即为0+1, 深度为1, 则这个递归停止，且向上返回
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    print(s.maxDepth(root))
