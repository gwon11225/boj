#include<stdio.h>

int main()
{
    int t;
    scanf("%d",&t);
    for(int a=0; a<t; a++)
    {
        int b,c;
        scanf("%d %d",&b,&c);
        printf("%d\n",b+c);
    }
}