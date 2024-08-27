from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        string = len(s)
        
        def reverse(start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
                
        reverse(0, string - 1)