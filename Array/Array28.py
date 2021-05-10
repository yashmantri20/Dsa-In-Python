class Solution:
    def trappingWater(self, height,n):
        # count = 0
        # for i in range(1,n-1):
        #     max_water = min(arr[i-1],max(arr[i+1:]))
        #     if arr[i] < max_water:
        #         count += max_water - arr[i] 
        #         arr[i] = max_water
        # return count
        l=0
        r=len(height)-1
        lmax,rmax=0,0
        count=0
        while l < r:
            if height[l]<height[r]:
                if height[l]>=lmax:
                    lmax=height[l]
                else:
                    count+=lmax-height[l]
                l+=1
            else:
                if height[r]>=rmax:
                    rmax=height[r]
                else:
                    count+=rmax-height[r]
                r-=1
        return count