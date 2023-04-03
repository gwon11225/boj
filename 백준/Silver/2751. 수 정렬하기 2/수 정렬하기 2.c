#include <stdio.h>
#include <stdlib.h>

int static compare (const void* first, const void* second)
{
    if (*(int*)first > *(int*)second)
        return 1;
    else if (*(int*)first < *(int*)second)
        return -1;
    else
        return 0;
}
int main(void)
{
    int N;
    scanf("%d",&N);
    int ar[N];
    for(int i = 0; i < N; i++){
        scanf("%d",&ar[i]);
    }
    qsort(ar,N,sizeof(int),compare);
    for(int i = 0; i < N; i++){
        printf("%d\n",ar[i]);
    }
    return 0;
}