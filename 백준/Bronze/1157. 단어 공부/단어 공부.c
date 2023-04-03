#include<stdio.h>

int main()
{
    char word[1000001] = { 0 };
    int abc[26] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
    scanf("%s",word);
    int a = 0;
    int b = 0;
    int sum = 0;
    int ncount = 0;
    char last;
    while(word[a] != '\0'){
        if (word[a] >= 'a' && word[a] <= 'z') word[a] -= 32;
        a++;
    }
    while(word[b] != '\0'){
        int m = word[b] - 'A';
        abc[m]++;
        b++;
    }
    for(int i = 0; i < 26; i++){
        if(abc[i] > sum){
            sum = abc[i];
        }
    }
    for(int j = 0; j < 26; j++){
        if(sum == abc[j]){
            ncount++;
            last = 'A' + j;
        }
    }
    if(ncount == 1) printf("%c",last);
    else printf("?");
    return 0;
}