class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = []
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if (nums[j]==target-nums[i]):
                    l.append(i)
                    l.append(j)
                    return l