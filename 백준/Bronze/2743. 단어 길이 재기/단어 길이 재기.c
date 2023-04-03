#include<stdio.h>

int main(){
    char String[101];
    int count = 0;
    scanf("%s",String);
    for(int i = 0;String[i] != 0;i++){
        count++;
    }
    printf("%d",count);
}