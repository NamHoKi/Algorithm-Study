#include "stdafx.h"
#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main() {
	int car = 0; // ��
	int goat1 = 1, goat2 = 2; // ����
	int r;   // �����ϴ� ��ȣ = ����
	int change; // 0 �ȹٲ� 1 �ٲ�
	int win0 = 0, lose0 = 0;  // �ȹٲ����� �� ��
	int win1 = 0, lose1 = 0;  // �ٲ����� �� ��
	int n;

	printf("���� �� : ");
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
	printf("<�ٲ��� ��>\n�� : %d\n�� : %d\n<�ȹٲ��� ��>\n�� : %d\n�� : %d\n", win1, lose1, win0, lose0);
	return 0;
}