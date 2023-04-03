#include <stdio.h>

int main()
{
    long int N;
    int count = 1;
    int sum = 1;
    scanf("%ld",&N);
    while(1){
        count++;
        if(N==1){
            printf("1");
            break;
        }
        else if(sum >= N){
            printf("%d",count - 1);
            break;
        }
        else{
            sum += (count - 2) * 6 + 6;
        }
    }
}