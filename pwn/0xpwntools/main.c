#include <stdio.h>
#include <stdlib.h>

void setup(){
    setbuf(stdin,0);
    setbuf(stdout,0);
    setbuf(stderr,0);
}

int main()
{
    char input[32];
    setup();
    puts("you have to use a special tool here, what is it?");
    read(0,input,32);
    if(input[0]){
        puts("great!!");
        system("/bin/sh");
    }

    return 0;
}
