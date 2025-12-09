import random
class Solution:

    def __init__(self, nums: List[int]):
    
        self.myList=[]
        self.resList=[]
        for i in nums:
            self.resList.append(i)
            self.myList.append(i)

    def reset(self) -> List[int]:
        self.myList=self.resList
        return self.myList

    def shuffle(self) -> List[int]:
        test=[]
        for i in self.myList:
            test.append(i)
        random.shuffle(test)
        return test
