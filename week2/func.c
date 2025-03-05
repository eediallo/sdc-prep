#include <stdio.h>


int sum(int a, int b){
	return a + b;
}



int main(){
	int a = 10;
	int b = 12;
	int result = sum(a, b);
	printf("result is: %d\n", result);
}
