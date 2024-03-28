from collections import UserList


class Solution:
    def numSubarrayProductLessThanK(self, nums: UserList[int], k: int) -> int:
        count = 0
        r = 0
        prod = 1
        for l in range(len(nums)):
            prod *= nums[l]

            while l <= r and prod > k:
                r += 1

            prod /= nums[l]
            count += r-l+1
        return count






# Driver code
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()

    # Example input
    nums = [10, 5, 2, 6]  # The input array
    k = 100  # The threshold for the product

    # Call the numSubarrayProductLessThanK method and print the result
    result = solution.numSubarrayProductLessThanK(nums, k)
    print(f"Number of subarrays with product less than {k}: {result}")