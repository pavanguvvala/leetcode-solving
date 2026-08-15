class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        time = requests[0]
        for i in range(len(requests)-1):
            time += abs(requests[i]-requests[i+1])
        return time