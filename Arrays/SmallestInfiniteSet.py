class SmallestInfiniteSet:

    def __init__(self):
        self.mySet=[]
        for i in range(1,1001):
            self.mySet.append(i)
        
    def popSmallest(self) -> int:
        val = self.mySet[0]
        self.mySet=self.mySet[1:]
        return val


    def addBack(self, num: int) -> None:
        test=0
        booleanVal = num not in self.mySet
        if booleanVal:
            
            for i in range(len(self.mySet)):
                if self.mySet[i] >  num:
                    test=i
                    break
            
            self.mySet.insert(test,num)
