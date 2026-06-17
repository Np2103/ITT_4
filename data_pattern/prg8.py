#include <stdio.h>
int count = 0;
double power(double x, unsigned int n)
{
    if (n == 0)
        return 1;
    double temp = power(x, n / 2);
    temp = temp * temp;
    count++;

    if (n % 2 == 1){
        temp = temp * x;
        count++;
    }
    return temp;
}

int main(){
    double x;
    unsigned int n;
    printf("Enter x: ");
    scanf("%lf", &x);
    printf("Enter power n: ");
    scanf("%u", &n);

    double result = power(x, n);
    printf("%.2lf ^ %u = %.2lf\n", x, n, result);
    printf("Number of multiplications: %d", count);

    return 0;
}
