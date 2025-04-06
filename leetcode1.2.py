class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)):
            for j in range(i +1, len(nums)):
                if nums[i] + nums[j] == target:
                    output.append(i)
                    output.append(j)
        return output

    nums=[1,4,6,8,9]
    target=12


    result=twoSum(nums,target)

    print(result)