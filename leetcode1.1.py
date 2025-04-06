from typing import List

# 修正后的 twoSum 函数
def twoSum(nums: List[int], target: int):  # 注意：移除了无用的 self 参数
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# ---------- 调用并打印结果 ----------
# 示例输入
nums = [2, 7, 11, 15]
target = 13

# 执行函数
result = twoSum(nums, target)

# 打印结果
print(f"输入: nums = {nums}, target = {target}")
print("输出:", result)