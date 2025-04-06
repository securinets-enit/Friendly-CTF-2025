#include <stdio.h>
#include <stdlib.h>
#include <signal.h>



void setup(){
	setbuf(stdin,0);
	setbuf(stdout,0);
	setbuf(stderr,0);
}

void vuln(){
	printf("you are trying to understand some stuff , but how??");
}

int main(int argc, char* argv[]){
	setup();
	vuln();
	exit(0);
	return 0;
}
