#include "stdafx.h"
#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main() {
	int n;
	int count;
	int x , y;
	int r; // ЗЃД§%4
	long int a; // ЦђБе
	long int sum = 0;

	srand((unsigned)time(NULL));

	scanf_s("%d", &n);

	for (int i = 0; i < 1000; i++) {
		count = 0;
		x = 0;
		y = 0;

		while (1) {
			count++;
			r = rand() % 4;

			if (r == 0)
				x++;
			else if (r == 1)
				x--;
			else if (r == 2)
				y++;
			else if (r == 3)
				y--;

			if (x == n || x == -n || y == n || y == -n)
				break;
		}
		sum += count;
	}
	a = sum / 1000;

	printf("%d\n", a);

	return 0;
}