class Solution:
    def isPalindrome(self, s: str) -> bool:

        newStr = ""                     # creates a new string

        for c in s:
            if c.isalnum():             # checks if the characteris alphanumeric
                newStr += c.lower()     # makes it all lowercase when adding to new string

        if newStr == newStr[::-1]:      # if the string is the same forward and reverse,
            return True                 # return True
        
        return False                    # otherwise, return False
        