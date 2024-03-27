class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        containsOne = False
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
            elif nums[i] == 1:
                containsOne = True

        if containsOne == False:
            return 1

        for i in range(n):
            num = abs(nums[i])
            idx = num - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1