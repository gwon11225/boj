#include<stdio.h>

int main(void)
{
    int a,b,c,d,e,f;
    scanf("%1d%1d%1d\n",&a,&b,&c);
    scanf("%1d%1d%1d\n",&d,&e,&f);
    int g = 100*a+10*b+c;
    int h = 100*d+10*e+f;
    printf("%d\n",g*f);
    printf("%d\n",g*e);
    printf("%d\n",g*d);
    printf("%d\n",g*h);
    
}