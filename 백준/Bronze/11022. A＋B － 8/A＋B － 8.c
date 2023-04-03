#include<stdio.h>

int main()
{
    int t;
    scanf("%d",&t);
    for(int a=1; a<=t; a++)
    {
        int b,c;
        scanf("%d %d",&b,&c);
        printf("Case #%d: %d + %d = %d\n",a,b,c,b+c);
    }
}