# *coding: utf-8 -*
# !@time: 2021-03-17 20:09:46
# !@author: miracleyin @email: [miracleyin@live.com](mailto:miracleyin@live.com)
# !@question title: pascals-triangle

# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。 
# 
#  
# 
#  在杨辉三角中，每个数是它左上方和右上方的数的和。 
# 
#  示例: 
# 
#  输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ] 
#  Related Topics 数组 
#  👍 462 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generate_math(self, numRows: int) -> List[List[int]]:
        ret = list()
        for i in range(numRows):
            row = list()
            for j in range(0, i + 1):
                if j ==0 or j == i:
                    row.append(1)
                else:
                    row.append(ret[i-1][j] + ret[i-1][j - 1])
            ret.append(row)
        return ret
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        res = [[1]]
        while len(res) < numRows:
            newRow = [a + b for a, b in zip([0] + res[-1], res[-1] + [0])]
            res.append(newRow)
        return res
# leetcode submit region end(Prohibit modification and deletion)
def main():
    numRows = 5
    res = Solution().generate(numRows)
    print(res)
main()