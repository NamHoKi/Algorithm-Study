#include "stdafx.h"
#include<stdio.h>

int main() {
	int n;

	printf("n : ");
	scanf_s("%d", &n);

	for (int i = 0; i <= n; i++) {
		if (i % 2 == 0) {
			for (int j = 0; j <= n; j++) {
				printf("%d %d\n", j, i);
			}
		}
		else {
			for (int j = n; j >= 0; j--) {
				printf("%d %d\n", j, i);
			}
		}
	}

	return 0;
}