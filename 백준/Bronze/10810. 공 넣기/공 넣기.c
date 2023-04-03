#include <stdio.h>

int main()
{
    int n,m;
    scanf("%d %d",&n,&m);
    int arr[n];
    for(int i = 0; i < sizeof(arr)/sizeof(int); i++){
        arr[i] = 0;
    }
    for(int A = 0; A < m; A++){
        int i,j,k;
        scanf("%d %d %d",&i,&j,&k);
        if(i == j){
            arr[i - 1] = k;
            continue;
        }
        for(int B = i - 1; B < j; B++){
            arr[B] = k;
        }
    }
    for(int C = 0; C < n; C++){
        printf("%d ",arr[C]);
    }
}