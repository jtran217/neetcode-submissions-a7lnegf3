class TimeMap:

    def __init__(self):
        self.m = defaultdict(list)  # key -> [(timestamp, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((timestamp, value))  # always increasing, no sort needed

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.m[key]
        lo, hi = 0, len(pairs) - 1
        result = ""
        while lo <= hi:
            mid = (lo + hi) // 2
            if pairs[mid][0] <= timestamp:
                result = pairs[mid][1]
                lo = mid + 1
            else:
                hi = mid - 1
        return result