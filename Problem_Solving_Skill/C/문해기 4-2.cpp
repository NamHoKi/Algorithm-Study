#include "stdafx.h"
#include<stdio.h>

int gcd(int a, int b) {
	if (a == 0)
		return b;
	return gcd(b%a, a);
}

int main() {
	int count = 0;
	
	for (int i = 2; i <= 98; i++) {
		for (int j = i + 1; j <= 99; j++) {
			for (int k = j + 1; k <= 100; k++) {
				if (gcd(i, j) == 1 && gcd(i, k) == 1 && gcd(j, k) == 1)
					count++;
			}
		}
	}
	printf("%d\n", count);

	return 0;
}