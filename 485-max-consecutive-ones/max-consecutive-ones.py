class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        res=0
        h=0
        for i in nums:
            if i==1:
                h+=1
            else:
                res=max(h,res)
                h=0
        return max(res,h)
        