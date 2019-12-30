#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/13 下午11:51
# @Title   : 543. 二叉树的直径
# @Link    : https://leetcode-cn.com/problems/diameter-of-binary-tree/


QUESTION = """
给定一棵二叉树，你需要计算它的直径长度。
一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。

示例 :
给定二叉树

          1
         / \
        2   3
       / \     
      4   5    
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

注意：两结点之间的路径长度是以它们之间边的数目表示。
"""


THINKING = """
第一思路是递归，左子树+右子树的深度就行了，后来提交多次都不对，经查阅发现并不是那么简单
首先树的直径的定义并不是从根节点开始的，直径的定义是某两个节点的最长路径，就是说把这个树"抻直"
当抻直的时候，这两个距离最远的子节点共有的内个节点才是直径的根节点，也就不能直接从给定的树的根节点直接开始计算

所以这里就一点特殊之处就在此，遍历的时候需要每次都判断一下左右部分能和起来一个最长的直径，也就是抻直了是不是最长的
用一个常量self.max_来计算最长直径这个数字，如果出现了更长直径的左右子树深度和就更新这个值
树的深度就是典型的递归问题，返回的是max(left_depth, right_depth) + 1
最后返回self.max_即可
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self. max_ = 0
        def depth(root):
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            self.max_ = max(self.max_, left + right)
            return max(left, right) + 1
        depth(root)
        return self.max_


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    print(s.diameterOfBinaryTree(root))
