class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        long_curr_seq=-999
        nums=set(nums)
        for i in nums:
            if i-1 not in nums:
                curr_seq=1
                while i+curr_seq in nums:
                    curr_seq+=1
                long_curr_seq=max(long_curr_seq, curr_seq)
        return max(0,long_curr_seq)

