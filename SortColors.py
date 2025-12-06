class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets=[[],[],[]]
        start=0
        mid=start+1
        end=len(nums)-1
        test=nums
        for i  in range(len(test)):
            if test[i] ==0:
                buckets[0].append(0)
            if test[i] ==1:
                buckets[1].append(1)
                
            if test[i] ==2:
                buckets[2].append(2)
        bucket=0
        start=0
        for bucket in range(3):
            nums[start:start+len(buckets[bucket])]=buckets[bucket]
            start+=len(buckets[bucket])
        print(nums)