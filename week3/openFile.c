#include <stdio.h>
#include <errno.h>
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

int main(){
	int file = open("hello.txt", O_WRONLY | O_CREAT);
	printf("%d", file);
}
