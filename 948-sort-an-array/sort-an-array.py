class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums)<=1:
            return nums
        mid=len(nums)//2
        left=nums[:mid]
        right=nums[mid:]
        left=self.sortArray(left)
        right=self.sortArray(right)
        return self.merge(left,right)
    def merge(self,left,right):
        m,n=len(left),len(right)
        i,j=0,0
        res=[]
        while i<m and j<n:
            if left[i]<=right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
        if i<m:
            while i<m:
                res.append(left[i])
                i+=1
        if j<n:
            while j<n:
                res.append(right[j])
                j+=1
        return res

        
        