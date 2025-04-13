#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>  // For sleep function
#include <sys/ptrace.h>
#include <sys/types.h>
#include <sys/wait.h>

// XOR decryption function
void another_one(unsigned char *data, int len, unsigned char key) {
    for (int i = 0; i < len; i++) {
        data[i] ^= key;
    }
}

// Caesar cipher decryption function (shift to the left)
void another_rabbit_hole(unsigned char *data, int len, int shift) {
    for (int i = 0; i < len; i++) {
        data[i] = data[i] - shift;  // Shift each byte to the left
    }
}

// Decryption function
void rabbit_hole(unsigned char *data, unsigned char *decrypted_data, int len, unsigned char key, int shift) {
    memcpy(decrypted_data, data, len); 
    another_rabbit_hole(decrypted_data, len, shift); 
    another_one(decrypted_data, len, key); // Apply XOR decryption
}

// Anti-debugging check
void anti_debug() {
    // Simple check for ptrace 
    if (ptrace(PTRACE_TRACEME, 0, NULL, NULL) == -1) {
        printf("Debugger detected! Exiting...\n");
        exit(1);
    }
}

// Simulate a loading bar
void loading_bar(const char *message) {
    printf("%s\n", message);
    for (int i = 0; i <= 100; i++) {
        usleep(10000);  // Simulate work being done
        printf("\r[%-10s] %d%%", "", i);
        fflush(stdout);
    }
    printf("\n");
}

int main() {
    // Anti-debugging function
    anti_debug();

    // Prompt message
    printf("Hello, aspiring hacker!\nYou will definetly decrypt the flag if you reverse the binary! or just ask nicely?\n ");
    
    printf("So I removed the debugging to make it a bit hard!\n");

    // Loading dependencies with a loading bar
    loading_bar("Loading my dependencies:");

    // Simulate user input prompt
    char user_input[100];
    printf("Do you want me to print the flag?:");
    fgets(user_input, sizeof(user_input), stdin); // Get user input

    // Simulate second loading bar
    loading_bar("I know you do, here youu are:");
    sleep(4);
    // Print fake kernel error
    printf("\nKernel Error: Critical failure during processing...\n");
    sleep(2);  // Simulate a small delay before proceeding

    // Encrypted message (just an example encrypted flag)
    unsigned char encrypted_message[] = {
        0xF9, 0xC3, 0xC9, 0xD3, 0xDA, 0xCF, 0xCE, 0xC3, 0xD4, 0xD9, 
        0xE3, 0xEE, 0xEF, 0xF4, 0xE1, 0x97, 0xFD, 0xD4, 0xD0, 0x98, 
        0xD3, 0xC5, 0xD0, 0xD4, 0xFD, 0x97, 0xFD, 0xD9, 0x94, 0x97, 
        0xC4, 0xFD, 0xCE, 0xCD, 0xFD, 0xC4, 0x99, 0xCA, 0xD3, 0xC5, 
        0xC5, 0x97, 0xCE, 0xC5, 0xFD, 0xD0, 0x99, 0xDA, 0x99, 0xDB
    };
    int len = sizeof(encrypted_message) / sizeof(encrypted_message[0]);
    unsigned char key = 0xA5; // XOR key
    int shift = 3; // Caesar cipher shift

    // Decrypted flag's buffer
    unsigned char decrypted_message[len + 1]; 

    // Decrypt the message
    rabbit_hole(encrypted_message, decrypted_message, len, key, shift);

    /*
    decrypted_message[len] = '\0';
    // Print the decrypted message (the flag)
    printf("Decrypted message: %s\n", decrypted_message);
    */
    return 0;
}

