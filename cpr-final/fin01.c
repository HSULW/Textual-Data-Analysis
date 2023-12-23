#include <stdio.h>
#include "frac.h"
#include <stdint.h>

int main() {
    int32_t result_x, result_y;

    // Example usage of frac_add
    int32_t a =-1, b = 2, c = 1, d = -3;

    int32_t add_result = frac_add(&result_x, &result_y, a, b, c, d);
    if (add_result == 0) {
        printf("frac_add result: %d / %d\n", result_x, result_y);
    } else {
        printf("Invalid input for frac_add\n");
    }

    int32_t del_result = frac_del(&result_x, &result_y, a, b, c, d);
    if (del_result == 0) {
        printf("frac_del result: %d / %d\n", result_x, result_y);
    } else {
        printf("Invalid input for frac_del\n");
    }

    int32_t mul_result = frac_mul(&result_x, &result_y, a, b, c, d);
    if (mul_result == 0) {
        printf("frac_mul result: %d / %d\n", result_x, result_y);
    } else {
        printf("Invalid input for frac_mul\n");
    }

    int32_t div_result = frac_div(&result_x, &result_y, a, b, c, d);
    if (div_result == 0) {
        printf("frac_div result: %d / %d\n", result_x, result_y);
    } else {
        printf("Invalid input for frac_div\n");
    }

    // Similar usage for frac_del, frac_mul, and frac_div can be added here

    return 0;
}
