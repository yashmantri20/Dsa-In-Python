# Given an array of size n and a number k, find all elements that appear more than " n/k " times.

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        total = len(nums) // 3
        output = []
        temp = list(set(nums))
        for i in temp:
            if nums.count(i) > total:
                output.append(i)
        return output

# Moore’s Voting Algorithm

def majorityElement(self, nums):
    if not nums:
        return []
    count1, count2, candidate1, candidate2 = 0, 0, 0, 1
    for n in nums:
        if n == candidate1:
            count1 += 1
        elif n == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = n, 1
        elif count2 == 0:
            candidate2, count2 = n, 1
        else:
            count1, count2 = count1 - 1, count2 - 1
    return [n for n in (candidate1, candidate2)
                    if nums.count(n) > len(nums) // 3]