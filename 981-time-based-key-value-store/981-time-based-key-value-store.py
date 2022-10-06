class TimeMap:

    def __init__(self):
        self.time_stamp = defaultdict(list)
        
    def binary_search(self, key, timestamp):
        arr = self.time_stamp[key]
        left, right = 0, len(arr) - 1
        
        while left < right:
            mid = left + (right - left + 1) // 2
            
            if arr[mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid
        
        if not arr or (left == 0 and arr[left][0] > timestamp):
            return ""
        return arr[left][1]
            
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_stamp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        return self.binary_search(key, timestamp)
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)