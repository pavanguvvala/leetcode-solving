class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while(low<high):
            cap = (low+high)//2
            cur_load = 0
            req_days = 1
            for w in weights:
                if cur_load + w <= cap:
                    cur_load+=w
                else:
                    cur_load = w
                    req_days+=1
            if (req_days<=days):
                high = cap
            else :
                low = cap + 1
        return low