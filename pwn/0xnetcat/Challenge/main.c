#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void setup(){
    setbuf(stdout,0);
    setbuf(stdin,0);
    setbuf(stderr,0);
}
int main()
{
    setup();
    system("cat banner.txt");
    system("/bin/sh");
    return 0;
}
