#include <stdio.h>
#include <stdlib.h>
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    
    static int arr[2];
    *returnSize = 2;
    for(int i=0;i<numsSize-1;i++){
        for(int i2=i+1;i2<numsSize;i2++){
            if (nums[i]+nums[i2] == target){
                arr[0]=i;
                arr[1]=i2;
                return arr;           
            }
        }
    }
    return NULL;
}
