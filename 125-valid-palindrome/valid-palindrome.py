class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([i.lower() for i in s if i.isalnum()])
        cmpp = list(s)
        left = 0
        right = len(cmpp) -1 
        while (left<right):
            cmpp[left],cmpp[right] = cmpp[right], cmpp[left]
            left+=1
            right-=1
        if "".join(cmpp) == s:
            return True
        else :
            return False