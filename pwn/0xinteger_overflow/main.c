#include <stdio.h>
#include <stdlib.h>

void setup(){
    setbuf(stdout,0);
    setbuf(stdin,0);
    setbuf(stderr,0);
} //don't mind this
unsigned int n,m;
int result;
int main()
{
    setup();
    printf("----DUMMMY CAL--------\n");
    printf("give me a number");
    scanf("%d",&n);
    if(n<0){
        printf("your number must be positive");
        exit(-1);
    }
    printf("give me another number");
    scanf("%d",&m);
    if (n<0){
        printf("your number must be positive");
        exit(-1);
    }
    result=n+m;
    if (result<0){
        printf("what?");
        system("/bin/sh");
    }
    return 0;
}
