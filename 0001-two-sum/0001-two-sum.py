class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
    # [2,7,11,15] target = 9
    #     []
        seen_hash = {}  #key,value
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in seen_hash:
                return [seen_hash[compliment], i]
            else:
                seen_hash[num] = i

#         [2,7,11,15]
#         #brute force :
#         for i in range(nums):
#             for j in range(i+1, nums):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]