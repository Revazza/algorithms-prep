class TimeMap:

    def __init__(self):
        self.container = {}

        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.container:
            self.container[key] = []

        self.container[key].append((timestamp, value))
        pass

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.container:
            return ""

        stamps = self.container[key]

        left = 0
        right = len(stamps) - 1

        while left <= right:
            mid = (right + left) // 2

            tm, val = stamps[mid]

            if tm == timestamp:
                return val
            elif tm > timestamp:
                right = mid - 1
            else:
                left = mid + 1

        if left == 0:
            return ""
        return stamps[left - 1][1]

