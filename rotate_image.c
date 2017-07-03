#include<stdio.h>

/*
Algo:
- do a transpose of the matrix
- swap row 1 with row 3
*/

int transpose(int);
int swap_rows(int);

void main(){
	int arr[3][3] = {0,1,2,3,4,5,6,7,8}; // array initialization
	int n = sizeof(arr)/sizeof(arr[0][0]); // length of 2D array
	printf("%d\n", n); 

	int arrr = transpose(arr);
	//arr = swap_rows(arr);
}

int transpose(int a){
	int t_a[3][3] = {1,2,3,4,5,6,7,8,9};
	return t_a;
}

int swap_rows(int a){
	int s_a[3][3] = {1,2,3,4,5,6,7,8,9};
	return s_a;
}