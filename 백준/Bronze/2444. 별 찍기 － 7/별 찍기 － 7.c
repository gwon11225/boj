#include <stdio.h>

int main()
{
	int n;
	scanf("%d", &n);

	for (int i = 1; i <= n ; i++)
	{
		for (int j = 1; j <= ((2 * n - 1) - (2 * i - 1)) / 2; j++)
		{
			printf(" ");
		}
		for (int j = 1; j <= 2 * i - 1; j++)
		{
			printf("*");
		}
		printf("\n");
	
	}
	for (int i = n + 1; i <= 2 * n - 1; i++)
	{
		for (int j = 1; j <= i - n; j++)
		{
			printf(" ");
		}
		for (int j = 1; j <= 4 * n - 2 * i - 1; j++)
		{
			printf("*");
		}
		printf("\n");
		
	}
}