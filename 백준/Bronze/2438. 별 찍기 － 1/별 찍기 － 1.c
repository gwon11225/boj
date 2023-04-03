#include<stdio.h>

int main()
{
    int f;
    scanf("%d",&f);
    for(int a=0; a<f; a++)
    {
        for(int b=0; b<=a; b++)
        {
            printf("*");
        }
        printf("\n");
    }
}