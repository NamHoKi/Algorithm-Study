#include "stdafx.h"
#include<stdio.h>

int main() {
	int n;
	int a,b,c;


	scanf_s("%d %d %d %d", &n, &a, &b, &c);
	
	if (a == 1 && b == 0 && c == 0) {
		for (int i = 0; i < n - 2; i++) {
			scanf_s("%d", &a);
			if (a == 1) {
				printf("Yes\n");
				return 0;
			}
		}
		printf("No\n");
	}
	else
		printf("No\n");

	return 0;
}