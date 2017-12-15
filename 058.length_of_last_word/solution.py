"""
Given a string s consists of upper/lower-case alphabets and empty space
characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space
characters only.

For example, Given s = "Hello World",
return 5.
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i = n - 1
        while i >= 0 and s[i].isspace():
            i -= 1
        res = 0
        while i >= 0 and not s[i].isspace():
            res += 1
            i -= 1
        return res