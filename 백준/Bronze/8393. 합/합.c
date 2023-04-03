#include<stdio.h>

int main(void)
{
    int a;
    scanf("%d",&a);
    int c=0;
    for(int b=1; b<=a; b++)
    {
        c=c+b;
    }
    printf("%d",c);
}