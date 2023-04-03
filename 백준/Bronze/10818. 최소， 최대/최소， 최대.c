#include <stdio.h>

int main(void) {
	int N, max=-1000000, min=1000000;
	scanf("%d", &N);
    int A[N];
	for (int i = 0; i < N; i++) {
		scanf("%d", &A[i]);
		if (A[i] > max)
			max = A[i];
		if (A[i] < min)
			min = A[i];
	}
	printf("%d %d", min, max);
}