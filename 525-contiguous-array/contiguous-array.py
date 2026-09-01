class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_length = 0
        first = {0: -1}
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            if count in first:
                length = i - first[count]
                max_length = max(max_length, length)
            else:
                first[count] = i
        return max_length