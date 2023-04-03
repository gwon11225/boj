#include<stdio.h>

void swap(int * a,int * b){
    int temp = *a;
    *a = *b;
    *b = temp;
}


int main(){
    int N,M;
    scanf("%d %d",&N,&M);
    int arr[N];
    for(int i = 1; i <= N; i++){
        arr[i - 1] = i;
    }
    for(int i = 0;i < M;i++){
        int a,b;
        scanf("%d %d",&a,&b);
        swap(&arr[a - 1],&arr[b - 1]);
    }
    for(int i = 0;i < N;i++){
        printf("%d ",arr[i]);
    }
}