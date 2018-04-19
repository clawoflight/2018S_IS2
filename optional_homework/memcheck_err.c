#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
	char* tmp = malloc(200);
	strcpy(tmp, "hello");
	free(tmp);
	puts(tmp);
	return 0;
}
