# *coding: utf-8 -*
# !@time: 2021-03-22 20:38:37
# !@author: miracleyin @email: [miracleyin@live.com](mailto:miracleyin@live.com)
# !@question title: binary-tree-level-order-traversal

# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。 
# 
#  
# 
#  示例： 
# 二叉树：[3,9,20,null,null,15,7], 
# 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回其层序遍历结果： 
# 
#  
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#  
#  Related Topics 树 广度优先搜索 
#  👍 815 👎 0

from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def generate_tree(self, nums):
        def level(index):
            if index >= len(nums):
                return None
            root = TreeNode(nums[index])
            root.left = level(2 * index + 1)
            root.right = level(2 * index + 2)
            return root
        return level(0)
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

# leetcode submit region end(Prohibit modification and deletion)
def main():
    p = TreeNode().generate_tree([3,9,20,'null','null',15,7])

    res = Solution().levelOrder(p)
    print(res)


main()