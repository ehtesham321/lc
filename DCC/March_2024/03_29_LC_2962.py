from collections import UserList


class Solution:
    def countSubarrays(self, nums: UserList[int], k: int) -> int:
        maxCount = res = l = 0
        maxElem = max(nums)
        for r in range(len(nums)):
            if nums[r] == maxElem:
                maxCount += 1

            while maxCount > k and l <= r:
                if nums[l] == maxElem:
                    maxCount -= 1
                l += 1

            if maxCount >= k:
                res += (r - l + 1)

        return res


# Example usage
solution = Solution()
nums = UserList([1,3,2,3,3])
k = 2
result = solution.countSubarrays(nums, k)
print(f"Number of subarrays: {result}")