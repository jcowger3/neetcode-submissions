class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        k = len(nums) -1
        j = int(i+k/2)
        count = 0
        if nums[i] == target:
            return i
        if nums[k] == target:
            return k

        while i < k and k != j and i != j:
            if nums[j] == target:
                return j

            if nums[j] > target:
                k = j
                j = int((i+k)/2)

            if nums[j] < target:
                i = j
                j = int((i+k)/2)
        
        return -1