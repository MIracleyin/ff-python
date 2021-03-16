# *coding: utf-8 -*
# !@time: 2021-03-14 10:44:17
# !@author: miracleyin @email: [miracleyin@live.com](mailto:miracleyin@live.com)
# !@question title: maximum-subarray

# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [0]
# 输出：0
#  
# 
#  示例 4： 
# 
#  
# 输入：nums = [-1]
# 输出：-1
#  
# 
#  示例 5： 
# 
#  
# 输入：nums = [-100000]
# 输出：-100000
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 3 * 104 
#  -105 <= nums[i] <= 105 
#  
# 
#  
# 
#  进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。 
#  Related Topics 数组 分治算法 动态规划 
#  👍 2990 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray_vio(self, nums: List[int]) -> int:
        pre, maxAns = 0, nums[0]
        for i in range(len(nums)):
            pre = max(pre + nums[i], nums[i])
            maxAns = max(maxAns, pre)
        return maxAns
    def maxSubArray_dp(self, nums: List[int]) -> int:
        n = len(nums)
        # 递归终止
        if n == 1:
            return nums[0]
        else:
            max_le = self.maxSubArray_dp(nums[0: len(nums) // 2])
            max_ri = self.maxSubArray_dp(nums[len(nums) // 2:len(nums)])

        max_l = nums[len(nums) // 2 - 1]
        tmp = 0
        for i in range(len(nums) // 2 - 1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        max_r = nums[len(nums) // 2]
        tmp = 0
        for i in range(len(nums) // 2, len(nums)):
            tmp += nums[i]
            max_r = max(tmp, max_r)
        return max(max_le, max_ri, max_l + max_r)
# leetcode submit region end(Prohibit modification and deletion)
def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    res = Solution().maxSubArray(nums)
    print(res)
main()