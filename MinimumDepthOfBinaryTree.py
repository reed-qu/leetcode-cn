#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/27 下午5:34
# @Title   : 111. 二叉树的最小深度
# @Link    : https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/


QUESTION = """
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.
"""


THINKING = """
这个题题设说的其实不是很好理解，并不是单纯的找最小深度而已
主要是要计算到  最近叶子节点  的最短路径，不是叶子节点的话，构不成这个路径
这也是为什么测试用例中的[1, 2]，结果是1，而不是0，因为1是根节点，2是叶子节点

这样也就是必须一直找到是叶子节点的内个几点，然后计算最短的路径，这样就分成几种情况

1. node.left is None 往右边找
2. node.right is None 往左边找
3. 如果左右都有的话，那就左右同时找

这3种情况还是有以下的要求的
1. 每次往下一层找的时候，深度要+1
2. 在一直往下找的过程中，找到叶子节点的时候，要返回最小深度的内个
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


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
    print(s.minDepth(root))
