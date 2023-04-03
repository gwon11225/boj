#include<stdio.h>
int main(void){
	int N,X,i,j;
	scanf("%d %d",&N,&X);
	int arnum[N];
	for(i=0;i<N;i++){
		scanf("%d",&arnum[i]);
        if (arnum[i] <X){
			printf("%d ",arnum[i]);
        }
    }
}