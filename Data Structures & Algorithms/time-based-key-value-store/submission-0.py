class TimeMap:

    def __init__(self):
        self.store = {} # key : list of [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        # checking if our list is empty
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:

        result = ""
        # we do this cuz if the key doesn't exist, 
        # the problem wants us to return an empty string

        # then we check what that list of values actually is
        values = self.store.get(key, [])

        # binary search
        left = 0
        right = len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if values[mid][1] <= timestamp: # then we know it's a valid value
                result = values[mid][0]
                left = mid + 1

            else: # if the value was bigger than timestamp
                right = mid - 1
                # no result assignment here cuz value is invalid

        return result
        
