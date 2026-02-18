#include <stdio.h>
#include <stdlib.h>
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    
    static int myArray[2];
    *returnSize = 2;
    for(int imdex = 0; index < numsSize - 1; index++){
        for(int index2 = index + 1; index2 < numsSize; index2++){
            if (nums[index] + nums[index2] == target){
                myArray[0] = index;
                myArray[1] = index2;
                return myArray;           
            }
        }
    }
    return NULL;
}
