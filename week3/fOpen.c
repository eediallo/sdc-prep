#include <stdio.h>
#include <errno.h>
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

int main(){
	FILE* pfptr;
	pfptr = fopen("hi.txt","w+");
	fprintf(pfptr, "%s", "to London");
}
