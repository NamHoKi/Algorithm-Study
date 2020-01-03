#include "stdafx.h"
#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main() {
	int car = 0; // Â÷
	int goat1 = 1, goat2 = 2; // ¿°¼Ò
	int r;   // ¼±ÅÃÇÏ´Â ¹øÈ£ = ·£´ý
	int change; // 0 ¾È¹Ù²Þ 1 ¹Ù²Þ
	int win0 = 0, lose0 = 0;  // ¾È¹Ù²åÀ»¶§ ½Â ÆÐ
	int win1 = 0, lose1 = 0;  // ¹Ù²åÀ»¶§ ½Â ÆÐ
	int n;

	printf("½ÇÇè ¼ö : ");
	scanf_s("%d", &n);

	srand((unsigned)time(NULL));

	for (int i = 0; i < n; i++) {
		r = rand() % 3;
		change = rand() % 2;
		if (r == 0) {
			if (change == 1)
				lose1++;
			else
				win0++;
		}
		else {
			if (change == 1)
				win1++;
			else
				lose0++;
		}
	}
	printf("<¹Ù²åÀ» ¶§>\n½Â : %d\nÆÐ : %d\n<¾È¹Ù²åÀ» ¶§>\n½Â : %d\nÆÐ : %d\n", win1, lose1, win0, lose0);
	return 0;
}