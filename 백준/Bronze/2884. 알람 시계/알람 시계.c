#include<stdio.h>

int main(void)
{
    int h,min;
    scanf("%d",&h);
    scanf("%d",&min);
    if(min<45 && h<1)
    {
        printf("%d %d",h+23,15+min);
    }
    else if(min<45)
    {
        printf("%d %d",h-1,15+min);
    }
    else
    {
        printf("%d %d",h,min-45);
    }
    
}