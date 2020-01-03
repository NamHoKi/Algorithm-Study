#include "stdafx.h"
#include<stdio.h>

int main() {
	int m[12] = { 31,28,31,30,31,30,31,31,30,31,30,31 };
	int birthday[3];
	int today[3];
	int bsum = 0;
	int tsum = 0;

	scanf_s("%d %d %d %d %d %d", &birthday[0], &birthday[1], &birthday[2], &today[0], &today[1], &today[2]);

	for (int i = 0; i < birthday[1]-1; i++) {
		bsum += m[i];
	}
	bsum += birthday[2];

	for (int i = 0; i < today[1]-1; i++) {
		tsum += m[i];
	}
	tsum += today[2];

	printf("%d\n", tsum - bsum + 365 * (today[0] - birthday[0]));

	return 0;
}