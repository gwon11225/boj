#include <stdio.h>

int main()
{
    int N;
    scanf("%d",&N);
    int sum = 0;
    char list[N+1];
    scanf("%s",list);
    for(int j = 0; j < N; j++)
    {
        switch(list[j])
        {
            case '1': 
                sum += 1;
                continue;
            case '2': 
                sum += 2;
                continue;
            case '3':
                sum += 3;
                continue;
            case '4':
                sum += 4;
                continue;
            case '5':
                sum += 5;
                continue;
            case '6':
                sum += 6;
                continue;
            case '7':
                sum += 7;
                continue;
            case '8':
                sum += 8;
                continue;
            case '9':
                sum += 9;
                continue;
            case '0':
                sum += 0;
                continue;
        }
    }
    printf("%d\n",sum);
}