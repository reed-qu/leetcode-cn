#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/11 下午6:07
# @Title   : 226. 翻转二叉树
# @Link    : https://leetcode-cn.com/problems/invert-binary-tree/


QUESTION = """
翻转一棵二叉树。

示例：
输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9

输出：
     4
   /   \
  7     2
 / \   / \
9   6 3   1

备注:
这个问题是受到 Max Howell 的 原问题 启发的 ：
谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。
"""


THINKING = """
递归解决，思想就是左右对调
递归的停止条件就是 root is None
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    print(s.invertTree(root))
