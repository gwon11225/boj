#include <stdio.h>

int main()
{
    int T;
    scanf("%d",&T);
    char s[21] = { 0 };
    int R;
    for(int i = 0; i < T; i++)
    {
        scanf("%d",&R);
        scanf("%s",s);
        int a = 0;
        while(s[a] != '\0')
        {
            for(int k = 0; k < R; k++)
            {
                printf("%c",s[a]);
            }
            a++;
        }
        printf("\n");
    }
}