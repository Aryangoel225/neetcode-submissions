class TimeMap:

    def __init__(self):
        # hashmap #key value (str) -> list of tuples each tuples is (timestamp (int), value (str))
        self.keyTime = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # add key with the tuple of timestamp + value
        self.keyTime[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        # use the key and then list of of tuples if doesn't exist return ""
        if key not in self.keyTime:
            return ""
        arr = self.keyTime[key]
        res = ""
        lo, hi  = 0 , len(arr) - 1
        target = timestamp
        while lo <= hi:
            mid = (lo + hi) // 2
            mid_time = arr[mid][0]
            if target == mid_time:
                return arr[mid][1]
            elif target >= mid_time:
                res = arr[mid][1]
                lo = mid + 1
            else:
                hi = mid - 1
       
        return res





        
