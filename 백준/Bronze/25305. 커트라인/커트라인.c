#include <stdio.h>

void change(int * a,int * b){
    int temp = *a;
    *a = *b;
    *b = temp;
};

void sort(int arr[],int size){
    for(int i = 0; i < size - 1; i++){
        for(int j = 0; j < (size - i) - 1; j++){
            if(arr[j] > arr[j + 1]){
                change(&arr[j],&arr[j + 1]);
            }
        }
    }
};



int main(void)
{
    int N,k;
    scanf("%d %d",&N,&k);
    int ar[N];
    for(int i = 0; i < N; i++){
        scanf("%d",&ar[i]);
    }
    sort(ar,sizeof(ar)/sizeof(int));
    printf("%d",ar[N-k]);
    return 0;
}