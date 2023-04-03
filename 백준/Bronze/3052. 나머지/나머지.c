#include<stdio.h>

int main()
{
    int list_1[10] = {0,};
    int list_2[42] = {0,};
    int r;
    int count = 0;
    for(int i = 0; i<10; i++)
    {
        scanf("%d\n",&list_1[i]);
    }
    for(int j = 0; j<10; j++)
    {
        r = list_1[j] % 42;
        list_2[r]++;
    }
    for(int k = 0; k<42; k++)
    {
        if(list_2[k] != 0){
            count++;
        }
    }
    printf("%d",count);
}