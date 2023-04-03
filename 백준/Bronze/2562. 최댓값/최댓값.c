#include <stdio.h>

int main()
{
    int list[9];
    int i;
    int max, idx;

    for (i = 0; i < 9; i++)
    {
        scanf("%d", &list[i]);
    }

    max = list[0];
    idx = 0;

    for (i = 0; i < 9; i++)
    {
        if (max < list[i])
        {
            max = list[i];
            idx = i;
        }
    }

    printf("%d\n%d\n", max, idx + 1);

    return 0;
}