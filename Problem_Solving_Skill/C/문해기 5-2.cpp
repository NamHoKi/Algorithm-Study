#include "stdafx.h"
#include<stdio.h>

int main() {
	int n;
	int min1, min2;;
	int x[100];
	int temp;
	scanf_s("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf_s("%d", &x[i]);

		if (i == 0)
			min1 = x[0];
		else if (i == 1 && min1 < x[1])
			min2 = x[1];
		else if (i == 1 && min1 >= x[1]) {
			temp = x[0];
			x[0] = x[1];
			x[1] = temp;
		}
			
		if (x[i] <= min1) {
			min2 = min1;
			min1 = x[i];
		}
		else if (x[i] > min1&&x[i] < min2)
			min2 = x[i];
	}
	printf("%d %d\n", min1, min2);

	return 0;
}