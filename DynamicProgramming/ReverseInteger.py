class Solution:
    def reverse(self, x: int) -> int:
        boolVal=False
        if x < 0:
            boolVal=True
            x*=-1
    
        finalVal=0
        i=0
        lst=[]
        while x>0:
            
            lst.append(x%10)
            i+=1
        
            x-=(x%10)
            x/=10
            x=int(x)
        i=len(lst)-1
        for val in lst:
            finalVal+=(val*(10**i))
            i-=1
        if boolVal:
            finalVal*=-1
        if finalVal > (2**31) - 1 or finalVal < - (2**31):
            return 0
        return finalVal   
