class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        if len(nums)<2:
            return dp[len(nums)-1]
        dp[1] = max(dp[0], nums[1])
        if len(nums)<3:
            return dp[len(nums)-1]
        for i in range(2,len(nums)):
            # This is the essential step
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[len(nums)-1]
