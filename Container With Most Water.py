class Solution:
    def maxArea(self, height: List[int]) -> int:
        vol , maxvol = 1, -999
        l=0
        r=len(height)-1
        while l<r:
            if height[l] < height[r]:
                vol=height[l] * ((r+1) - (l+1))
                maxvol = max(vol,maxvol)
                l+=1

            else:
                vol=height[r] * ((r+1) - (l+1))
                maxvol = max(vol,maxvol)
                r-=1
        return max(maxvol,0)