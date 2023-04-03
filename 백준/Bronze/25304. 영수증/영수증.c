#include<stdio.h>

int main()
{
    int a,b;
    int f=0;
    scanf("%d%d",&a,&b);
    for(int c=0; c<b; c++){
        int d,e;
        scanf("%d%d",&d,&e);
        int g=d*e;
        f += g;
    }
    if(a==f)
    {
        printf("Yes");
    }
    else
    {
        printf("No");
    }
}