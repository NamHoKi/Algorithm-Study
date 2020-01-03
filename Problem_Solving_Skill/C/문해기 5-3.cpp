#include "stdafx.h"
#include<stdio.h>
#include<math.h>

int main() {
	int n;
	int sum = 0;
	double a;
	double sd = 0.0;
	int x[100];

	scanf_s("%d", &n);

	for (int i = 0; i< n; i++) {
		scanf_s("%d", &x[i]);

		sum += x[i];
	}
	a = (double)sum / n;

	for (int i = 0; i < n; i++) {
		sd += (double)(a - x[i])*(a - x[i]);
	}
	sd = sqrt((double)sd / n);

	printf("%lf %lf\n", a, sd);

	return 0;
}