#include "stdafx.h"
#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main() {
	long int count=0, count1 = 0, count2 = 0;
	int r; // ·£´ý%6+1
	double a1, a2;

	srand((unsigned)time(NULL));

	for (long int i = 0; i < 1000000; i++) {
		for (int j = 0; j < 6; j++) {
			r = rand() % 6 + 1;
			if (r == 1)
				count++;
		}
		if (count >= 1)
			count1++;
		count = 0;
		for (int j = 0; j < 12; j++) {
			r = rand() % 6 + 1;
			if (r == 1)
				count++;
		}
		if (count >= 2)
			count2++;
		count = 0;
	}
	a1 = (double)count1 / 1000000;
	a2 = (double)count2 / 1000000;
	printf("%lf %lf\n", a1,a2);

	return 0;
}