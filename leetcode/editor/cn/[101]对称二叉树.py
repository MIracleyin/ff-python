# *coding: utf-8 -*
# !@time: 2021-03-20 21:55:14
# !@author: miracleyin @email: [miracleyin@live.com](mailto:miracleyin@live.com)
# !@question title: symmetric-tree

# 给定一个二叉树，检查它是否是镜像对称的。 
# 
#  
# 
#  例如，二叉树 [1,2,2,3,4,4,3] 是对称的。 
# 
#      1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#  
# 
#  
# 
#  但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的: 
# 
#      1
#    / \
#   2   2
#    \   \
#    3    3
#  
# 
#  
# 
#  进阶： 
# 
#  你可以运用递归和迭代两种方法解决这个问题吗？ 
#  Related Topics 树 深度优先搜索 广度优先搜索 
#  👍 1297 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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

class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        def check(left, right):
            if left and not right:
                return False
            elif not left and right:
                return False
            elif not left and not right:
                return True
            else:
                return left.val == right.val and check(left.left, right.right) and check(left.right, right.left)

        if not root:
            return True
        return check(root.left, root.right)

# leetcode submit region end(Prohibit modification and deletion)
def main():
    p = TreeNode().generate_tree([1, 2, 3, 4, 5])

    res = Solution().isSymmetric(p)
    print(res)


main()