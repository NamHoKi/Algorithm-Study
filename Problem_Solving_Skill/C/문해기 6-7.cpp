#include "stdafx.h"
#include<stdio.h>

int main() {
	int a[20], b[20];
	int a1, b1;
	int a2, b2;
	int c1 = 0, c2 = 0;

	scanf_s("%d %d", &a1, &b1);

	a2 = a1;
	b2 = b1;
	for (int i = 0; i < 20; i++) {
		a[i] = a1 % 10;
		a1 /= 10;
		c1++;
		if (a1 == 0)
			break;
	}

	for (int i = 0; i < 20; i++) {
		b[i] = b2 % 10;
		b1 /= 10;
		c2++;
		if (b1 == 0)
			break;
	}

	while (1) {
		if (a[c1] < b[c2]) {
			printf("%d %d\n", a2, b2);
			break;
		}
		else if (a[c1] > b[c2]) {
			printf("%d %d\n", b2, a2);
			break;
		}

		if (c1 == 0) {
			printf("%d %d\n", a2, b2);
			break;
		}

		if (c2 == 0) {
			printf("%d %d\n", b2, a2);
			break;
		}
		c1--;
		c2--;
	}

	return 0;
}