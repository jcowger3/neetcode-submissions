class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dict = {}

        for num in nums:
            if num in dict:
                val = dict[num]
                dict[num] = val + 1
            else:
                dict[num] = 1

        # print(dict)
        output = []

        for i in range(k):
            max_key = max(dict, key=dict.get)
            output.append(max_key)
            dict.pop(max_key)

        return output
