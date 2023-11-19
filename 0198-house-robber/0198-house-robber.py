class Solution:
    def rob(self, nums: List[int]) -> int:

        N = len(nums)

        # Edge case 1
        if N == 0:
            return 0
        
        # Edge case 2
        if N == 1:
            return nums[0]

        dp = [0] * N

        # Base cases
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])

        # Recursive cases
        if N > 2:
            i = 2
            while i < N:
                dp[i] = max(dp[i-2] + nums[i], dp[i-1])
                i += 1

        return max(dp)

        return 1        


        
        