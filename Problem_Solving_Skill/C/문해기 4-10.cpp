#include "stdafx.h"
#include<stdio.h>

int main() {
	int x[4],y[4];
	int area;
	int temp;

	for (int i = 0; i < 4; i++) {
		scanf_s("%d %d", &x[i], &y[i]);
	}
	
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 3; j++) {
			if (x[j] < x[j + 1]) {
				temp = x[j];
				x[j] = x[j + 1];
				x[j + 1] = temp;
			}
			if (y[j] < y[j + 1]) {
				temp = y[j];
				y[j] = y[j + 1];
				y[j + 1] = temp;
			}
		}
	}
	
	printf("%d\n", (x[1] - x[2])*(y[1] - y[2]));

	return 0;
}