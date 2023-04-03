#include <stdio.h>

void set(int ar[],int N){
    for(int i = 0;i < N;i++){
        ar[i] = i + 1;
    }
}

void swap(int * a,int * b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main()
{
    int N,M;
    scanf("%d %d",&N,&M);
    int arr[N];
    set(arr,N);
    for(int i = 0;i < M;i++){
        int first,second;
        scanf("%d %d",&first,&second);
        int loop = second - first;
        for(int j = 0;j < loop;j++){
            swap(&arr[first - 1],&arr[second - 1]);
            first++;
            second--;
            if(first >= second){
                break;
            }
        }
    }
    for(int i = 0;i < N;i++){
        printf("%d ",arr[i]);
    }
}