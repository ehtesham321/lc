from collections import UserList


class Solution:
    def firstMissingPositive(self, nums: UserList[int]) -> int:
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


# Create an instance of the Solution class
solution = Solution()

# Define a list of numbers to test the method
nums = [3, 2, -1, 1]

# Call the firstMissingPositive method with the test list and print the result
missing_positive = solution.firstMissingPositive(nums)
print(f"The first missing positive integer is: {missing_positive}")