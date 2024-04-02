class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        if len(s) != len(t):
            return False
        s_to_t = {}
        t_to_s = {}
        for i in range(n):
            if s[i] in s_to_t and s_to_t[s[i]] != t[i]:
                return False
            if t[i] in t_to_s and t_to_s[t[i]] != s[i]:
                return False

            s_to_t[s[i]] = t[i]
            t_to_s[t[i]] = s[i]

        return True

# Runner code
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    s1 = "egg"
    t1 = "add"
    print(f"Is '{s1}' isomorphic to '{t1}'? {solution.isIsomorphic(s1, t1)}")  # Expected: True

    # Test case 2
    s2 = "foo"
    t2 = "bar"
    print(f"Is '{s2}' isomorphic to '{t2}'? {solution.isIsomorphic(s2, t2)}")  # Expected: False

    # Test case 3
    s3 = "paper"
    t3 = "title"
    print(f"Is '{s3}' isomorphic to '{t3}'? {solution.isIsomorphic(s3, t3)}")  # Expected: True

    # Asserts will raise an AssertionError if the condition is False
    assert solution.isIsomorphic("egg", "add") == True, "Test case 1 failed"
    assert solution.isIsomorphic("foo", "bar") == False, "Test case 2 failed"
    assert solution.isIsomorphic("paper", "title") == True, "Test case 3 failed"
    assert solution.isIsomorphic("badc", "baba") == False, "Test case 4 failed"
    assert solution.isIsomorphic("13", "42") == True, "Test case 5 failed"

    print("All test cases passed!")