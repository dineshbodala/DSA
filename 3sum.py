import collections
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        uniq_dict = collections.defaultdict()
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                if nums[i]+nums[l]+nums[r]==0:
                    if (nums[i],nums[l],nums[r]) not in uniq_dict:
                        uniq_dict[tuple([nums[i],nums[l],nums[r]])]=1
                    l+=1
                    r-=1

                elif nums[i]+nums[l]+nums[r]<0:
                    l+=1
                
                else:
                    r-=1

        return uniq_dict.keys()



