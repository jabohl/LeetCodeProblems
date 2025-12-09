class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        myDict={}
        for i in nums:
            myDict[i]=[]
        for i in range(len(nums)):
            myDict[nums[i]].append(i)
        lst=[]
        for val in myDict:
            if len(myDict[val])>len(nums)/3:
                lst.append(val)
        return lst