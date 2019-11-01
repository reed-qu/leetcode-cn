#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/1 上午10:23
# @Title   : 100. 相同的树
# @Link    : https://leetcode-cn.com/problems/same-tree/


QUESTION = r"""
给定两个二叉树，编写一个函数来检验它们是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:
输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]
输出: true

示例 2:
输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]
输出: false

示例 3:
输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]
输出: false
"""


THINKING = r"""
二叉树，二者结构和数值完全一样才是相同的，这类遍历可迭代对象的问题大部分是可以用递归来解决
首先特殊情况 如果p, q均为None的话，即为True
如果二者其一为None的话，即为False
最后是递归停止条件，当前节点相同，即继续递归，全都相同才为相同，如果有一处不同，即可结束递归返回False
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    t1 = TreeNode(7)
    left1 = TreeNode(3)
    right1 = TreeNode(4)
    left1.left = TreeNode(0)
    left1.right = TreeNode(3)
    right1.left = TreeNode(1)
    right1.right = TreeNode(3)
    t1.left = left1
    t1.right = right1

    t2 = TreeNode(7)
    left2 = TreeNode(3)
    right2 = TreeNode(4)
    left2.left = TreeNode(0)
    left2.right = TreeNode(3)
    right2.left = TreeNode(1)
    right2.right = TreeNode(3)
    t2.left = left2
    t2.right = right2

    s = Solution()
    print(s.isSameTree(t1, t2))
