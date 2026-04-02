class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = [[pos, spe] for pos, spe in zip(position, speed)]    # list comprehension - array of pairs

        stack = []

        for pos, spe in sorted(pair)[::-1]:     # reverse sorted order -> adds O(logn) time
                                                # reverse order cuz we start with car closest to destination
                                                # and work right-to-left to check interceptions / fleets
            stack.append((target - pos) / spe)  # single slash for decimal division

            if len(stack) >= 2 and stack[-1] <= stack[-2]:  # if the car at top of stack reaches destination
                                                            # before the car ahead of it (index -2)
                                                            # also len >= 2 cuz if only 1 car then only 1 fleet / no comparison  
                stack.pop()

        return len(stack) 

        # time O(nlogn) -> n for iterating thru the given array, logn for using sorted()
        # space O(n) for creating our pair and stack