class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for i, num in enumerate(nums):
            if i == 0:
                dict[num] = i
            else:
                if target - num in dict:
                    return [dict[target - num], i]
                else:
                    dict[num] = i