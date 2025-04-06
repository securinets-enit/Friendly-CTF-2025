#include <stdio.h>

void vuln() {
    char buffer[64];

    puts("asslema");
    gets(buffer);

    printf(buffer);
    puts("");

    puts("zidni");
    gets(buffer);
}

int main() {
    vuln();
}

void win() {
    puts("mabrouk 3lik");
    system("/bin/sh");
}
