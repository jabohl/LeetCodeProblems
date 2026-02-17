#include <stdio.h>
#include <math.h>
#include <limits.h>

int reverse(int x) {
    int rev = 0;
    if (x < 0) {
        x = -x;
        rev = 1;
    }
    int intVal = 0;
    int sumVal = 0;
    int val = 0;
    int test = x;

    while (x > 0) {
        val += 1;
        x -= (x % 10);
        x /= 10;
    }

    while (test > 0) {
        sumVal += (test % 10) * (int)pow(10, val - 1);
        val -= 1;
        test /= 10;
    }

    if (rev) {
        sumVal = -sumVal;
    }

    if (sumVal > INT_MAX || sumVal < INT_MIN) {
        return 0;
    }
    return sumVal;
}
