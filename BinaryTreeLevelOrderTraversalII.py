#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 下午1:34
# @Title   : 107. 二叉树的层次遍历 II
# @Link    : https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/


QUESTION = r"""
给定一个二叉树，返回其节点值自底向上的层次遍历。（即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
   
返回其自底向上的层次遍历为：
[
  [15,7],
  [9,20],
  [3]
]
"""


THINKING = """
硬逻辑实现即可
这里想要一层一层的循环处理下去，直接的思路是一如一个current_layer变量，记录当前处理到的层，如果没有的话，那就表示处理结束了
current_layer中可能存在多个node，一个一个node的处理下去，当前层的val都记录到cur_layer_val中
下一层的左右节点记录到 next_layer_node 中，这样在每一次层循环结束之前，把当前的值cur_layer_val添加到result头部
下一层next_layer_node是需要继续处理的，那就赋值给current_layer继续处理
最后返回result
"""


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        current_layer = [root]

        while current_layer:
            cur_layer_val = []
            next_layer_node = []

            for node in current_layer:
                if node:
                    cur_layer_val.append(node.val)
                    next_layer_node.extend([node.left, node.right])
            if cur_layer_val:
                result.insert(0, cur_layer_val)
            current_layer = next_layer_node
        return result


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    print(s.levelOrderBottom(root))
