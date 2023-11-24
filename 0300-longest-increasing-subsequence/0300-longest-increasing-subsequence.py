class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        dp[-1] = 1

        for i in range(len(nums) - 2, -1, -1):
        
            cur_max = 0
            for k in range(i+1, len(nums)):
                if dp[k] >= cur_max and nums[i] < nums[k]:
                    cur_max = dp[k]
            dp[i] = 1 + cur_max
        
        return max(dp)