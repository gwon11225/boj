#include <stdio.h>

int main()
{
    int arr[100][100] = { 0 };
    int arr_2[2];
    int num;
    int count = 0;
    scanf("%d",&num);
    for(int i = 0; i < num; i++){
        scanf("%d %d",&arr_2[0],&arr_2[1]);
        for(int i = arr_2[0]; i < arr_2[0] + 10; i++){
            for(int j = arr_2[1]; j < arr_2[1] + 10; j++){
                arr[i][j] = 1;
            }
        }
    }
    for(int i = 0; i < 100; i++){
        for(int j = 0; j < 100; j++){
            if(arr[i][j] == 1){
                count++;
            }
        }
    }
    printf("%d",count);
}