#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/15 下午10:54
# @Title   : 617. 合并二叉树
# @Link    : https://leetcode-cn.com/problems/merge-two-binary-trees/


QUESTION = """
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

示例 1:

输入: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  

输出: 
合并后的树:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7

注意: 合并必须从两个树的根节点开始。
"""


THINKING = """
递归的构建一个合并树就可以了
首先停止条件就是二者其一若为None则返回另一个树
然后跟节点手动构建，依次递归的往下构建left节点和right节点
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1

        root = TreeNode(t1.val + t2.val)
        root.left = self.mergeTrees(t1.left, t2.left)
        root.right = self.mergeTrees(t1.right, t2.right)
        return root


if __name__ == '__main__':
    s = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    print(s.mergeTrees(t1, t2))
