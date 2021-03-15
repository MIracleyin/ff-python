### 解题思路
本题给定一个**排序**数组和 target 值，如果 target 在数组中，找出其索引，否则将 target 插入到数组中，返回插入位置。对**二分查找**有所了解的童鞋，看到**排序数组**，眼中是不是**冒光**了，这不就可以**二分查找**去做嘛。

### 二分查找
二分查找写法有多种，但比较流行的主要有**两种**，即**递归版本**和**非递归版本**。假设数组是升序排列的，且数组中只存在一个目标值，则这**两种版本的代码模板**如下：

**递归版本代码模板**
```c
int binarySearch(int* nums, int low, int high, int target) {
    if (low > right) {
        return -1;
    }
 
    /* 防止两个接近 2147483647 的整形数相加，出现溢出的风险 */
    int mid = low + (high - low) / 2;  
    /* 目标值小于数组中间值，则在数组的前半区间查找 */
    if (nums[mid] > target) {           
        return binarySearch(nums, low, mid - 1, target);
    /* 目标值大于数组中间值，则在数组的后半区间查找 */
    } else if (nums[mid] < target) {   
        return binarySearch(nums, mid + 1, high, target);
    /* 目标值等于数组中间值，查找到目标值，直接返回 */
    }  else if (nums[mid] == target) {
        return mid;
    }    
}
```
**非递归版本**根据**查找区间是左闭右闭还是左闭右开**又可以分为两种

**非递归版本代码模板（查找区间左闭右闭）**
```c
int binarySearch(int* nums, int numsSize, int target) {
    if (nums == NULL || numsSize <= 0) {
        return -1;
    }
 
    /* 在 [low...high] 的范围里查找 target */
    int low = 0, high = numsSize - 1;
    /* 当 low == high 时，区间 [low...high] 依然是有效的 */
    while (low <= high) {      
        /* 防止整型溢出 */                       
        int mid = low + ((high - low) >> 1); 
        /* 找到要查找的元素，直接返回 */   
        if (nums[mid] == target) {            
            return mid;
        /* 中间元素大于要查找的元素，去 mid 左侧 [low, mid - 1] 查找 */         
        } else if (nums[mid] > target) {      
            high = mid - 1;
        /* 中间元素小于要查找的元素，去 mid 右侧 [mid + 1, high] 查找 */  
        } else if (nums[mid] < target) {        
            low = mid + 1;                      
        }
    }
    return -1;
}
```
**非递归版本代码模板（查找区间左闭右开）**
```c
int binarySearch(int* nums, int numsSize, int target) {
    if (nums == NULL || numsSize <= 0) {
        return -1;
    }
 
    /* 在 [low...high) 的范围里查找 target */
    int low = 0, high = numsSize;
    /* 当 low == high 时，区间 [low...high) 依然是无效的 */
    while (low < high) {      
        /* 防止整型溢出 */                       
        int mid = low + ((high - low) >> 1); 
        /* 找到要查找的元素，直接返回 */   
        if (nums[mid] == target) {            
            return mid;
        /* 中间元素大于要查找的元素，去 mid 左侧 [low, mid) 查找 */         
        } else if (nums[mid] > target) {      
            high = mid;
        /* 中间元素小于要查找的元素，去 mid 右侧 [mid + 1, high) 查找 */  
        } else if (nums[mid] < target) {        
            low = mid + 1;                      
        }
    }
    return -1;
}
```
写**非递归版本**的**二分查找代码的核心**在于：**清晰定义左右边界 low 和 high 具体表达的含义，在循环查找中就需要不断维护这个含义**。

在循环中不断维护 low 和 high 的含义，也就是说在循环中保证了一个**循环不变量**。

**循环不变量**
![image.png](https://pic.leetcode-cn.com/1615538060-dIUjtS-image.png)

### 本题注意点
如果 target 没在该排序数组中，二分查找最后返回的是 left 还是 right？
查找区间是左闭右闭 [left, right]，以 [1,3,5,6], 0 为栗子，如下图示：
![image.png](https://pic.leetcode-cn.com/1615536586-aDYonn-image.png)

**nums[mid] = 3 > 0, right 左移到 mid - 1**
![image.png](https://pic.leetcode-cn.com/1615536780-lQvAIi-image.png)

**此时 nums[mid] = 1 > 0，跳出循环应该直接返回 left，好像 right 也可以。插入后数组如下图示**
![image.png](https://pic.leetcode-cn.com/1615537227-NmJSjS-image.png)

### Show me the Code（左闭右闭）
```c []
int searchInsert(int* nums, int numsSize, int target){
    int left = 0, right = numsSize - 1;
    while (left <= right) {
        int mid = left + ((right - left) >> 1);
        if (nums[mid] == target) {
            return mid;
        } else if(nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return left;
}
```
```cpp []
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
};
```
```java []
class Solution {
    public int searchInsert(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = left + ((right - left) >> 1);
            if (nums[mid] == target) {
                return mid;
            } else if(nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
}
```
```python3 []
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left
```
```go []
func searchInsert(nums []int, target int) int {
    left, right := 0, len(nums) - 1
    for left <= right {
        mid := (right - left) >> 1 + left
        if nums[mid] == target {
            return mid
        } else if nums[mid] < target {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    return left
}
```

### Show me the Code（左闭右开）
```c []
int searchInsert(int* nums, int numsSize, int target){
    int left = 0, right = numsSize;
    while (left < right) {
        int mid = left + ((right - left) >> 1);
        if (nums[mid] == target) {
            return mid;
        } else if(nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left;
}
```
```c++ []
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0, right = nums.size();
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
};
```
```java []
class Solution {
    public int searchInsert(int[] nums, int target) {
        int left = 0, right = nums.length;
        while (left < right) {
            int mid = left + ((right - left) >> 1);
            if (nums[mid] == target) {
                return mid;
            } else if(nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
}
```
```python3 []
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left
```
```go []
func searchInsert(nums []int, target int) int {
    left, right := 0, len(nums)
    for left < right {
        mid := (right - left) >> 1 + left
        if nums[mid] == target {
            return mid
        } else if nums[mid] < target {
            left = mid + 1
        } else {
            right = mid
        }
    }
    return left
}
```
**更多精彩内容，请关注 微信公众号：TanLiuYi00**

**如果感觉题解对你有帮助，不要吝啬给一个👍哦！**