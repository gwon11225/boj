#include<stdio.h>

int main(){
    char String[1001];
    int index;
    scanf("%s",String);
    scanf("%d",&index);
    printf("%c",String[index - 1]);
}