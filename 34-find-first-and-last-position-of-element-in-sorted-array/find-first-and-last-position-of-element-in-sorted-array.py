class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        while (low < high) :
            mid = int((low+high)/2)
            if (nums[mid]>=target):
                high = mid
            else :
                low = mid + 1
        first_oc = low

        if (first_oc == len(nums) or nums[first_oc]!=target) :
            return [-1, -1]
        
        low = 0
        high = len(nums)
        while (low<high) :
            mid = int((low+high)/2)
            if (nums[mid]>target):
                high = mid
            else :
                low = mid + 1
        last_oc = low - 1

        return [first_oc, last_oc]
