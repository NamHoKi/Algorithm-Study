#include "stdafx.h"
#include<stdio.h>

int main() {
	int n;
	int count[10] = { 0 };

	scanf_s("%d", &n);

	for (;;) {
		if (n / 10 == 0)
			break;
		count[n % 10]++;
		n /= 10;
	}

	for (int i = 0; i < 10; i++) {
		printf("%d ", count[i]);
	}
	printf("\n");

	return 0;
}