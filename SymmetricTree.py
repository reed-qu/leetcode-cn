#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 下午3:42
# @Title   : 101. 对称二叉树
# @Link    : https://leetcode-cn.com/problems/symmetric-tree/


QUESTION = """
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

说明:
如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
"""


THINKING = """
采用递归的方式
首先如果是空树则是对称的
然后判断左右两个子树，left, right
如果left, right二者都是null，那么是可以的，返回True
如果left, right二者有其中一个是null，那么不可以，返回False
然后比较的就是当前节点的值一样 且 left左==right右 且 left右==right左
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def sub_isSymmetric(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and \
                   sub_isSymmetric(left.left, right.right) and \
                   sub_isSymmetric(left.right, right.left)
        return sub_isSymmetric(root.left, root.right)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    print(s.isSymmetric(root)) # 此部分没有实现树结构
