#include<stdio.h>

void gen_fibonacci(int first, int second, int total);

void main(){

	int first=0, second=1, total;

	//printf("Enter first 2 number\n");
	//scanf("%d %d", &first, &second);

	printf("Enter number of total terms to be printed\n");
	scanf("%d", &total);

	gen_fibonacci(first, second, total);
}

void gen_fibonacci(int first, int second, int total){
	int sum, counter = 0;
	int new = 0;

	while(counter < total){
		sum = first + second;
		first = second;
		second = sum;

//		printf("%d %d\n", new, sum);
		for(int i=new+1; i<sum; i++){
			printf("%d\n", i);
		}
//		printf("%d\n", sum);
		counter ++;
		new = sum;
	}
}
