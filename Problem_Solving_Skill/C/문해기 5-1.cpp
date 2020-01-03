#include "stdafx.h"
#include<stdio.h>

int main() {
	int n;
	int k;
	int index;
	int x[100];
	int c = -1000;
	int count = 0;
	
	scanf_s("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf_s("%d", &x[i]);
	}

	scanf_s("%d", &k);

	for (int i = 0; i < n; i++) {
		if (k == x[i]) {
			index = i;
			c = x[i];
			break;
		}

		if (c < x[i] && x[i] < k) {
			index = i;
			c = x[i];
			count++;
		}

		if (i==n-1&&count==0) {
			printf("-1\n");
			return 0;
		}
	}

	if (k - c < 0)
		printf("%d %d %d\n", index, c, c - k);
	else
		printf("%d %d %d\n", index, c, k - c);

	return 0;
}
