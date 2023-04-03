#include <stdio.h>

int main()
{
    char String[101];
    while(gets(String) != NULL){
        printf("%s\n",String);
    }
}