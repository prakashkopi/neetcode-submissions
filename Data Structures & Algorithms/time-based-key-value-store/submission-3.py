class TimeMap:
    # hashmap + binary search
    # try with tuple instead
    # "foo" --> ("bar", 1)
    def __init__(self):
        self.cache= {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        # avoids key not found error when a new key is inserted
        if key not in self.cache:
            self.cache[key]= []
        self.cache[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # binary search to find ts value since the constraint is 
        # All the timestamps of set are strictly increasing.
        # this means the array is sorted, so we can use BS for O(logn)
        res= ''
        if key not in self.cache: 
            return res
            
        values= self.cache[key]
        l, r= 0, len(values)-1

        while l <= r: 
            m= (l+r) // 2
            m_ts= values[m][1]

            # if match is found, return the string value
            if m_ts == timestamp: 
                return values[m][0]
            # too small, check right half of list
            elif m_ts < timestamp: 
                res= values[m][0] # will end with closest smaller value to timestamp
                l= m + 1
            else: 
                r= m-1
        return res

        

        