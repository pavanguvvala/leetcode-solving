class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        low_r = 0
        high_r = n - 1
        while (low_r<=high_r):
            mid_r = (low_r + high_r)//2
            if (matrix[mid_r][0] <= target and matrix[mid_r][m-1]>= target):
                low = 0
                high = m - 1
                while(low<=high):
                    mid = (low+high)//2
                    if (matrix[mid_r][mid]==target):
                        return True
                    elif matrix[mid_r][mid] < target:
                        low = mid + 1
                    else:
                        high = mid - 1
                return False
            elif (matrix[mid_r][m-1]<target):
                low_r = mid_r + 1
            else :
                high_r = mid_r - 1
        return False
