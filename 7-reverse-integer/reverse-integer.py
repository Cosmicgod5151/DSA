class Solution:
    def reverse(self, x: int) -> int:
        res=0
        num=-1 if x<0 else 1
        x=abs(x)
        while(x>0):
            ld=x%10
            res=(res*10)+ld
            x=x//10
        res=num*res
        if res<-2**31 or res>2**31:
            return 0
        return res
        