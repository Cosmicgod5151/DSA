class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n=len(nums)
        array=[0]*n
        j=0
        for i in range(0,n):
            if(nums[i]>0):
                array[j]=nums[i]
                j+=1
        for i in range(0,n):
            if(nums[i]<0):
                array[j]=nums[i]
                j+=1
        j = 0
        k = n // 2

        for i in range(n // 2):
            nums[j] = array[i]
            nums[j + 1] = array[k]

            j += 2
            k += 1

        return nums



        