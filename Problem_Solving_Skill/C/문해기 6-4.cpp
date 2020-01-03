#include "stdafx.h"
#include<stdio.h>

int main() {
	int n;
	int x[100] = { 0 };
	int temp;

	scanf_s("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf_s("%d", &x[i]);
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n-1; j++) {
			if (x[j] > x[j + 1]) {
				temp = x[j];
				x[j] = x[j + 1];
				x[j + 1] = temp;
			}
		}
	}

	for (int k = 0; k < 10; k++) {
		for (int i = 0; i < n; i++) {
			if (x[i] == x[i + 1] && x[i] != -1) {
				for (int j = i; j < n; j++) {
					x[j] = x[j + 1];
				}
			}
		}
	}


	for (int i = 0; i < n; i++) {
		if (x[i]==0)
			return 0;
		printf("%d ", x[i]);
	}
}