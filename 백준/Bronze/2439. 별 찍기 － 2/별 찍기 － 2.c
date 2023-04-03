#include<stdio.h>

int main()
{
    int f;
    scanf("%d",&f);
    for(int a=0; a<f; a++)
    {
        for(int b=a; b<f-1; b++)
        {
            printf(" ");
        }
        for(int c=0; c<=a; c++ )
        {
            printf("*");
        }
        printf("\n");
    }
}