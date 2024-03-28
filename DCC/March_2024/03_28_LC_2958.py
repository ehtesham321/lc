from collections import UserList


class Solution:
    def maxSubarrayLength(self, nums: UserList[int], k: int) -> int:
        good = 0
        count_map = {}
        noOutOfBounds = 0
        l = 0
        for r in range(len(nums)):
            count = count_map.get(nums[r],0) + 1
            count_map[nums[r]] = count
            if count > k:
                noOutOfBounds += 1
            while l <= r and noOutOfBounds > 0:
                count = count_map.get(nums[l],0)
                if count > k and (count - 1) <= k:
                    noOutOfBounds -= 1
                count_map[nums[l]] = count_map.get(nums[l], 0) - 1
                l += 1
            good = max(good, r - l + 1)
        return good

if __name__ == "__main__":
    # Instantiate the Solution class
    solution = Solution()

    # Define the nums array and k value for testing
    nums = [2, 2, 2, 3]  # Example array
    k = 1  # Example k value

    # Call the maxSubarrayLength method and store the result
    max_length = solution.maxSubarrayLength(nums, k)

    # Print the result
    print(f"The length of the longest subarray with no more than {k} occurrences of any element is: {max_length}")
