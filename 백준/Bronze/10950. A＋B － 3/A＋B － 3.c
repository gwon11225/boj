#include<stdio.h>

int main(void)
{
    int a;
    scanf("%d",&a);
    for(int b=0; b<a; b++)
    {
        int c,d;
        scanf("%d %d",&c,&d);
        printf("%d \n",c+d);
    }
}