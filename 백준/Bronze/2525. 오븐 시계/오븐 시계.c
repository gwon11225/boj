#include<stdio.h>

int main(void)
{
    int h,min,t;
    scanf("%d %d",&h,&min);
    scanf("%d",&t);
    int a = min + t;
    if(h+a/60>=24&&a>=60)
    {
        printf("%d %d",h+a/60-24,a%60);
    }
    else if(a>=60)
    {
        printf("%d %d",h+a/60,a%60);
    }
    else
    {
        printf("%d %d",h,a);
    }
    
}