#include <stdio.h>

void change(int * a,int * b){
    int temp = *a;
    *a = *b;
    *b = temp;
};

int sort(int arr[],int size){
    for(int i = 0; i < size - 1; i++){
        for(int j = 0; j < (size - i) - 1; j++){
            if(arr[j] > arr[j + 1]){
                change(&arr[j],&arr[j + 1]);
            }
        }
    }
};


int main(){
    int sum = 0;
    int aver;
    int ar[5];
    for(int i = 0; i < 5; i++){
        scanf("%d",&ar[i]);
    }
    sort(ar,sizeof(ar)/sizeof(int));
    for(int i = 0; i < 5; i++){
        sum += ar[i];
        aver = sum/5;
    }
    printf("%d\n%d",aver,ar[2]);
}