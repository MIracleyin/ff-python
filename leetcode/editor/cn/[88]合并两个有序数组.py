# *coding: utf-8 -*
# !@time: 2021-03-16 08:58:57
# !@author: miracleyin @email: [miracleyin@live.com](mailto:miracleyin@live.com)
# !@question title: merge-sorted-array

# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。 
# 
#  初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nu
# ms2 的元素。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# 输出：[1,2,2,3,5,6]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums1 = [1], m = 1, nums2 = [], n = 0
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  nums1.length == m + n 
#  nums2.length == n 
#  0 <= m, n <= 200 
#  1 <= m + n <= 200 
#  -109 <= nums1[i], nums2[i] <= 109 
#  
#  Related Topics 数组 双指针 
#  👍 801 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def merge_lng(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:m+n] = sorted(nums1[:m] + nums2[:n])
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        nums1_copy = nums1[:m]
        nums1[:] = []
        p1, p2 = 0, 0
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1
        if p1 < m:
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]
        print(nums1)
# leetcode submit region end(Prohibit modification and deletion)

def main():
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    res = Solution().merge(nums1, 3, nums2,3)
    print(res)
main()