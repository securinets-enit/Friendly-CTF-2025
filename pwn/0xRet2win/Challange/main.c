#include <stdio.h>
#include <stdlib.h>

void setup(){
   setbuf(stdout,0);
   setbuf(stdin,0);
   setbuf(stderr,0);
}
void vuln(){
    char buffer[16];
    printf("where is my mind?\n");
    gets(buffer);
}

void win(){
    printf("how??");
    system("/bin/sh");
}
int main()
{
    setup();
    vuln();
    return 0;
}
