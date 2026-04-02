class Solution:

    # parameter: strs: a list of strings
    # return: encode a list of strings to a single string.
    def encode(self, strs: List[str]) -> str:
        
        result = ""     # our result is a single string
        for s in strs:

            # our method is to track the length of each string
            # and use a delimiter "#".
            # we do this so the string itself can contain integers 
            # and the symbol or wtv we use as our delimiter 
            # without messing up the encoding
            result += str(len(s)) + "#" + s
        return result

    # parameter: str: a single string
    # return: decodes a string to a list of strings
    def decode(self, s: str) -> List[str]:
        
        result = []       # our result is a list of strings
        i = 0           # we use this pointer to tell us what position we're at in strs

        while i < len(s):

            # we know the start of the string is an integer
            # so we want to find the delimiter

            j = i
            while s[j] != "#":
                j += 1              # we increment til we find the "#"
            
            # then when we get to the pound
            # we get the int of the string from index i to j
            length = int(s[i:j])

            # now we know how many characters following j that we need to read
            # in order to contain the entire string
            result.append(s[j + 1 : j + 1 + length])
            # j + 1 cuz j is at the delimiter
            # and we go til the end of the length which we just recorded

            # now we need to move our pointer i to the next string
            i = j + 1 + length

        return result

    # this runs in O(n) time cuz we go thru each string once
    # also O(n) space but that's part of the output so idk if it matters





