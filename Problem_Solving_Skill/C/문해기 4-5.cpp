#include "stdafx.h"
#include<stdio.h>

int main() {
	int n;
	int count1, count2 = 0;
	int x;

	scanf_s("%d", &n);

	for (int i = 1; i <= n; i++) {
		x = i;
		count1 = 0;
		while (1) {     // iÀÇ ÀÚ¸´¼ö
			x = x / 10;
			count1++;
			if (x == 0)
				break;
		}

		x = i;
		for (int j = 0; j < count1; j++) {
			if (x % 10 == 0)
				count2++;
			x = x / 10;
		}
	}
	printf("%d\n", count2);

	return 0;
}