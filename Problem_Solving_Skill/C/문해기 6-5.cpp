#include "stdafx.h"
#include<stdio.h>

int main() {
	int n;
	int x[50][2];
	int temp;

	scanf_s("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf_s("%d %d", &x[i][0], &x[i][1]);
	}

	for (int i = 0; i < n*n; i++) {
		for (int j = 0; j < n - 1; j++) {
			if (x[j][0] > x[j + 1][0]) {
				temp = x[j][0];
				x[j][0] = x[j + 1][0];
				x[j + 1][0] = temp;

				temp = x[j][1];
				x[j][1] = x[j + 1][1];
				x[j + 1][1] = temp;
			}

			if (x[j][0] == x[j + 1][0]) {
				if (x[j][1] > x[j + 1][1]) {
					temp = x[j][0];
					x[j][0] = x[j + 1][0];
					x[j + 1][0] = temp;

					temp = x[j][1];
					x[j][1] = x[j + 1][1];
					x[j + 1][1] = temp;
				}
			}
		}
	}


	for (int i = 0; i < n; i++) {
		printf("%d %d\n", x[i][0], x[i][1]);
	}
	printf("\n");

	return 0;
}