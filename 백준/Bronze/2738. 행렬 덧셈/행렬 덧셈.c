#include <stdio.h>

int main()
{
    int size[2];
    scanf("%d %d",&size[0],&size[1]);
    int arr_1[size[0]][size[1]];
    int arr_2[size[0]][size[1]];
    int answer[size[0]][size[1]];
    for(int i = 0; i < size[0]; i++){
        for(int j = 0; j < size[1]; j++){
            scanf("%d",&arr_1[i][j]);
        }
    }
    for(int i = 0; i < size[0]; i++){
        for(int j = 0; j < size[1]; j++){
            scanf("%d",&arr_2[i][j]);
        }
    }
    for(int i = 0; i < size[0]; i++){
        for(int j = 0; j < size[1]; j++){
            answer[i][j] = arr_1[i][j] + arr_2[i][j];
            printf("%d ",answer[i][j]);
        }
        printf("\n");
    }
}