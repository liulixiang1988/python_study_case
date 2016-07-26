/* sample.c */
#include <math.h>

/* 计算最大因子 */
int gcd(int x, int y) {
    int g = y;
    while(x > 0) {
        g = x;
        x = y % x;
        y = g;
    }
    return g;
}

/* 测试（x0, y0)是否是mandelbrot集合， Zn+1=(Zn)^2+C */
int in_mandel(double x0, double y0, int n) {
    double x=0, y=0, xtemp;
    while(n > 0){
        xtemp = x*x - y*y + x0;
        y = 2*x*y + y0;
        x = xtemp;
        n -= 1;
        if (x*x + y*y > 4) return 0;
    }
    return 1;
}

/* 两个数相除 */
int divide(int a, int b, int *remainder) {
    int quot = a /b;
    *remainder = a % b;
    return quot;
}

/* 求数组的均值 */
double avg(double *a, int n) {
    int i;
    double total = 0.0;
    for(i = 0; i < n; i++) {
        total += a[i];
    }
    return total / n;
}

/* 结构体 */
typedef struct Point {
    double x, y;
} Point;

/* 调用结构体的函数 */
double distance(Point *p1, Point *p2) {
    return hypot(p1->x - p2->x, p1->y - p2->y);
}