# find duplicate in an array of N+1 Integers

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1
            if d[i] > 1:
                return i


nums.sort()
for i in range(len(nums)):
    if nums[i] == nums[i+1]:
        return nums[i]
                