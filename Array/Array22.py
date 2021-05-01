# Maximum Product Subarray
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
        curr_max = curr_min = all_max = arr[0]
        for ele in arr[1:]:  
            curr_max, curr_min = max(curr_max * ele, curr_min * ele, ele), min(curr_max * ele, curr_min * ele, ele)
            all_max = max(all_max, curr_max)
            
        return all_max
