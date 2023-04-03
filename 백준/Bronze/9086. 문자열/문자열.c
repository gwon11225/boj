#include<stdio.h>

int main(){
    char word[1001];
    int n;
    scanf("%d",&n);
    for(int i = 0;i < n;i++){
        int count = 0;
        scanf("%s",word);
        for(int j = 0;word[j] != 0;j++){
            count++;
        }
        printf("%c%c\n",word[0],word[count - 1]);
    }
}