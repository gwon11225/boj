#include <stdio.h>

int main()
{
    int arr[9][9];
    int max = 0;
    int whr[2];
    for(int i = 0; i < 9; i++){
        for(int j = 0; j < 9; j++){
            scanf("%d",&arr[i][j]);
        }
    }
    for(int i = 0; i < 9; i++){
        for(int j = 0; j < 9; j++){
            if(arr[i][j] >= max){
                max = arr[i][j];
                whr[0] = i;
                whr[1] = j;
            }
        }
    }
    printf("%d\n%d %d",max,whr[0]+1,whr[1]+1);
}