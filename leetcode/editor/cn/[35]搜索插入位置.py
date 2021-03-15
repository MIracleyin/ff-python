# *coding: utf-8 -*
# !@time: 2021-03-13 20:15:42
# !@author: miracleyin @email: [miracleyin@live.com](mailto:miracleyin@live.com)
# !@question title: search-insert-position

# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。 
# 
#  你可以假设数组中无重复元素。 
# 
#  示例 1: 
# 
#  输入: [1,3,5,6], 5
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: [1,3,5,6], 2
# 输出: 1
#  
# 
#  示例 3: 
# 
#  输入: [1,3,5,6], 7
# 输出: 4
#  
# 
#  示例 4: 
# 
#  输入: [1,3,5,6], 0
# 输出: 0
#  
#  Related Topics 数组 二分查找 
#  👍 845 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchInsert_lcrc(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1 #
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else: # nums[mid] < target
                left = mid + 1
        return left
    def searchInsert_lcro(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)#
        while left < right: # 和lcrc的区别
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left
    def searchInsert_vio(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if (nums[i] >= target):
                return i
        return len(nums)
    def searchInsert_rec(self, nums: List[int], target: int, low: int, high: int) -> int:
        if low > high:
            return -1
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.searchInsert_rec(nums, target, low, mid - 1)
        else:
            return self.searchInsert_rec(nums, mid + 1, high, target)

# leetcode submit region end(Prohibit modification and deletion)
def main():
    nums = [1, 3, 5, 6]
    target = 2
    res = Solution().searchInsert_rec(nums, target, 0, 3)
    print(res)
main()