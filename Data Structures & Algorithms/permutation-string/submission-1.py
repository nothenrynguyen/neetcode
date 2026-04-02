class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # if s1 is longer, no substring of s2 can be a permutation
        if len(s1) > len(s2):
            return False

        # frequency count of characters in s1
        s1Count = [0] * 26

        # frequency count of the current window in s2
        windowCount = [0] * 26

        # build the frequency map for s1
        for char in s1:
            s1Count[ord(char) - ord('a')] += 1

        left = 0  # left pointer of the sliding window

        # expand the window by moving the right pointer
        for right in range(len(s2)):
            # add the new character to the window
            windowCount[ord(s2[right]) - ord('a')] += 1

            # if the window is larger than s1, shrink it from the left
            if right - left + 1 > len(s1):
                windowCount[ord(s2[left]) - ord('a')] -= 1
                left += 1

            # if the character frequencies match, we found a permutation
            if windowCount == s1Count:
                return True

        return False
