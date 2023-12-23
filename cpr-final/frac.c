#include "frac.h"
#include <limits.h>

int32_t gcd(int32_t a, int32_t b) {
    while (b != 0) {
        int32_t temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int32_t reduce_fraction(int32_t *numerator, int32_t *denominator) {
    int32_t common_factor = gcd(*numerator, *denominator);
    *numerator /= common_factor;
    *denominator /= common_factor;

    if (*denominator < 0) {
        *numerator *= -1;
        *denominator *= -1;
    }

    if ((*denominator > INT_MAX / common_factor) || (*denominator < INT_MIN / common_factor) ||
        (*numerator > INT_MAX / common_factor) || (*numerator < INT_MIN / common_factor)) {
        return -1;  // 溢位
    }

    return 0;  // 成功完成簡化
}

int32_t frac_add(int32_t *x, int32_t *y, int32_t a, int32_t b, int32_t c, int32_t d) {
    if (b == 0 || d == 0) {
        return -1;
    }

    *x = a * d + c * b;
    *y = b * d;

    if (reduce_fraction(x, y) != 0) {
        return -1;  // 溢位
    }

    return 0;
}

int32_t frac_del(int32_t *x, int32_t *y, int32_t a, int32_t b, int32_t c, int32_t d) {
    if (b == 0 || d == 0) {
        return -1;
    }

    *x = a * d - c * b;
    *y = b * d;

    if (reduce_fraction(x, y) != 0) {
        return -1;  // 溢位
    }

    return 0;
}

int32_t frac_mul(int32_t *x, int32_t *y, int32_t a, int32_t b, int32_t c, int32_t d) {
    if (b == 0 || d == 0) {
        return -1;
    }

    *x = a * c;
    *y = b * d;

    if (reduce_fraction(x, y) != 0) {
        return -1;  // 溢位
    }

    return 0;
}

int32_t frac_div(int32_t *x, int32_t *y, int32_t a, int32_t b, int32_t c, int32_t d) {
    if (b == 0 || d == 0 || c == 0) {
        return -1;
    }

    *x = a * d;
    *y = b * c;

    if (reduce_fraction(x, y) != 0) {
        return -1;  // 溢位
    }

    return 0;
}
