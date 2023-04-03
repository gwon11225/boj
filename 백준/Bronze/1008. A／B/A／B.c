#include<stdio.h>

int main(void)
{
    int A,B;
    scanf("%d",&A);
    scanf("%d",&B);
    double C = ((double)A / (double)B);
    printf("%.9lf",C);
}