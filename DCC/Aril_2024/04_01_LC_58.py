#Problem Link : https://leetcode.com/problems/length-of-last-word/description/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1:][0])

solution = Solution()

str = " Hello! from the Other Side   "

length = solution.lengthOfLastWord(str)

print(f"The length of the last word of the string \"{str}\" is :{length}")