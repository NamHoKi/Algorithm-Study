#include "stdafx.h"
#include<stdio.h>

int main() {
	int x[1000];
	int temp;
	int count = 0;

	while (1) {
	loop:
		scanf_s("%d", &x[count]);
		if (x[count] == -1)
			return 0;
		if (count != 0) {
			for (int i = 0; i < count; i++) {
				if (x[count] == x[i]) {
					printf("duplicte entry\n");
					goto loop;
				}
			}
		}

		for (int i = 0; i < count; i++) {
			for (int j = 0; j < count; j++) {
				if (x[j] > x[j + 1]) {
					temp = x[j];
					x[j] = x[j + 1];
					x[j + 1] = temp;
				}
			}
		}

		for (int i = 0; i <=count; i++) {
			printf("%d ", x[i]);
		}
		printf("\n");
		count++;
	}
	printf("\n");
	return 0;
}