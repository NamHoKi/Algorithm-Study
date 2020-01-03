#include "stdafx.h"
#include<stdio.h>

int main() {
	int n;
	int x[100];
	int k;
	int min = 1000;
	int index;

	scanf_s("%d", &n);
	
	for (int i = 0; i < n; i++) {
		scanf_s("%d", &x[i]);
	}
	scanf_s("%d", &k);

	for (int i = 0; i < n; i++) {
		if ((k - x[i] < 0) && (x[i] - k < min)) {
			min = x[i] - k;
			index = i;
		}
		else if ((k - x[i] >= 0) && (k - x[i] < min)) {
			min = k - x[i];
			index = i;
		}
	}

	printf("%d\n", x[index]);

	return 0;
}