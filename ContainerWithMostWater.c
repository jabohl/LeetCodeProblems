#include <stdio.h>

int maxArea(int* height, int heightSize) {
    int maxContainer = 0;
    int i1 = 0;
    int i2 = heightSize - 1;
    while (i2 != i1) {
        int minHeight = height[i1] < height[i2] ? height[i1] : height[i2];
        int maxTest = (i2 - i1) * minHeight;
        if (maxTest > maxContainer) {
            maxContainer = maxTest;
        }
        if (height[i2] > height[i1]) {
            i1++;
        } else {
            i2--;
        }
    }
    return maxContainer;
}
