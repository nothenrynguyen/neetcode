class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) - 1

        while left < right:
            
            while left < right and not self.alphaNum(s[left]):      # need to use "self" to call a function inside an object
                left += 1

            while right > left and not self.alphaNum(s[right]):
                right -= 1
            
            if s[left].lower() != s[right].lower():                 # use lower() to compare only lowercase
                return False

            left += 1       # if there's a match then
            right -= 1      # increment / dec both
        
        return True
    

    def alphaNum(self, c):
        
        if (ord('A') <= ord(c) <= ord('Z') or     # checks if the character is alphaNumeric
            ord('a') <= ord(c) <= ord('z') or     # in case the interview doesnt want us to
            ord('0') <= ord(c) <= ord('9')):      # use the isalnum function in python
            return True
        return False                              # can just return the condition (automatically sets to True/False)
                                                  # but this syntax is easier for me to read