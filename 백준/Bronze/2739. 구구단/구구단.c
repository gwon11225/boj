#include<stdio.h>

int main(void)
{
    int a;
    scanf("%d",&a);
    int b=1;
    while(b<=9)
    {
        printf("%d * %d = %d\n",a,b,a*b);
        b++;
    }
}