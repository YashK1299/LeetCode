"""
    You are given an integer array nums and an integer target.
    You want to build an expression out of nums by adding one of the symbols '+' and '-' before each
    integer in nums and then concatenate all the integers.
    For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them
    to build the expression "+2-1".
    Return the number of different expressions that you can build, which evaluates to target.

    Example 1:
        Input: nums = [1,1,1,1,1], target = 3
        Output: 5
        Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
        -1 + 1 + 1 + 1 + 1 = 3
        +1 - 1 + 1 + 1 + 1 = 3
        +1 + 1 - 1 + 1 + 1 = 3
        +1 + 1 + 1 - 1 + 1 = 3
        +1 + 1 + 1 + 1 - 1 = 3

    Example 2:
        Input: nums = [1], target = 1
        Output: 1

    Constraints:
        1 <= nums.length <= 20
        0 <= nums[i] <= 1000
        0 <= sum(nums[i]) <= 1000
        -1000 <= target <= 1000
"""


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
            DP Approach:
                T(n) = O(2^n)
                T(n) = O(n)
        """
        if len(nums) == 1:
            return 1 if nums[0] == target or nums[0] == -target else 0
        if len(nums) == 2:
            res = 0
            if nums[0] + nums[1] == target:
                res += 1
            if -nums[0] - nums[1] == target:
                res += 1
            if nums[0] - nums[1] == target:
                res += 1
            if nums[1] - nums[0] == target:
                res += 1
            return res
        return self.findTargetSumWays(nums[:len(nums)-1], target-nums[-1]) + self.findTargetSumWays(nums[:len(nums)-1],target+nums[-1])

    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
        """
            DP Approach using knapsack intuition:
                T(n) = O(n^2)
                S(n) = O(n*(target + sum(nums)))
        """
        s = sum(nums)
        if target > s or target < -s or (target+s)%2 != 0:
            return 0
        goal = (target + s)//2
        C = [[0 for i in range(goal+1)] for j in range(len(nums)+1)]
        for i in range(len(nums)+1):
            C[i][0] = 1
        for i in range(1, len(nums)+1):
            for j in range(goal+1):
                if nums[i-1] > j:
                    C[i][j] = C[i-1][j]
                else:
                    C[i][j] = C[i-1][j] + C[i-1][j-nums[i-1]]
        return C[-1][goal]

    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        """
            1D DP Approach using knapsack intuition:
                T(n) = O(n^2)
                S(n) = O(target + sum(nums))
        """
        s = sum(nums)
        if target > s or target < -s or (target+s)%2 != 0:
            return 0
        goal = (target + s)//2
        C = [0 for i in range(goal+1)]
        C[0] = 1
        for i in range(len(nums)):
            nextt = [0 for j in range(goal+1)]
            for j in range(goal+1):
                if nums[i] > j:
                    nextt[j] = C[j]
                else:
                    nextt[j] = C[j] + C[j-nums[i]]
            C = nextt
        return C[goal]
