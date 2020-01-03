#include "stdafx.h"
#include<stdio.h>

int main() {
	int k;
	int count = 0;
	int a = 1;

	printf("k : ");
	scanf_s("%d", &k);

	while (1) {
		for (int i = 0; i <= count; i++) {
			printf("%d %d\n",i,count-i);
		}
		if (count == k)
			break;

		count++;
	}

	return 0;
}