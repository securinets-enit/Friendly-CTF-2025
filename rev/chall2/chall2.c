#include <stdio.h>
#include <string.h>
#include <math.h>

#define FIRST_FLAG "SecurinetsENIT{just_str1ngs_n0thing_srs}"
#define XOR_KEY 0x5A
#define FLAG_SIZE 44
#define MAX_INPUT_LEN 100

// Correct encrypted flag bytes for the third flag
unsigned char encrypted_flag[FLAG_SIZE] = {
    0x5b, 0x80, 0xa3, 0xf2, 0x4a, 0xc0, 0x6e, 0x3e, 0x5c, 0xa6,
    0x05, 0xe3, 0x01, 0x83, 0x7b, 0x98, 0x37, 0x3a, 0xa4, 0x8c,
    0x02, 0xb7, 0x62, 0x68, 0x21, 0x13, 0x35, 0xa4, 0xdb, 0xce,
    0x6f, 0xcd, 0xe7, 0xe3, 0x74, 0x40, 0xc3, 0x1c, 0x72, 0xb6,
    0x68, 0x93, 0xca, 0x54
};

// XOR encryption function that returns the encrypted result
unsigned char* xor_encrypt(const char* input, int len_input, int key) {
    static unsigned char encrypted_result[MAX_INPUT_LEN];

    for (int i = 0; i < len_input; i++) {
        encrypted_result[i] = input[i] ^ key;
    }

    return encrypted_result;  // Return the encrypted result
}

// Decryption function for the third flag
void decrypt_flag(unsigned char *encrypted_flag_in, unsigned char *decrypted_flag) {
    for (int i = 0; i < FLAG_SIZE; i++) {
        decrypted_flag[i] = (unsigned char)((int)encrypted_flag_in[i] - (int)pow(i + 2, 3)) % 256;
    }
}

int main(void) {
    char input[MAX_INPUT_LEN];
    
    // First flag
    printf("Je mange, tu manges. Ta3tini flags, na3tik points.Mrigl?");
    scanf("%99s", input);
	
    printf("Okay, give me the first flag:\n");
    scanf("%99s", input);
    
    if (strcmp(input, FIRST_FLAG) != 0) {
        printf("Incorrect flag, sorry :(\n");
        printf("See you next time. Quitting...\n");
        return 0;
    }

    printf("Okaayyyyyyyyy letsssssssssss go! You got it right\n");
    
    // Second flag (XOR part)
    printf("So, can you give me the second flag? Please? :3\n");
    scanf("%99s", input);

    int len_input = strlen(input);
    
    // Encrypt the input using XOR
    unsigned char* encrypted_input = xor_encrypt(input, len_input, XOR_KEY);
    
    // Define each byte of the expected XOR result as separate variables
    unsigned char byte_1 = 0x09;
    unsigned char byte_2 = 0x3f;
    unsigned char byte_3 = 0x39;
    unsigned char byte_4 = 0x2f;
    unsigned char byte_5 = 0x28;
    unsigned char byte_6 = 0x33;
    unsigned char byte_7 = 0x34;
    unsigned char byte_8 = 0x3f;
    unsigned char byte_9 = 0x2e;
    unsigned char byte_10 = 0x29;
    unsigned char byte_11 = 0x1f;
    unsigned char byte_12 = 0x14;
    unsigned char byte_13 = 0x13;
    unsigned char byte_14 = 0x0e;
    unsigned char byte_15 = 0x21;
    unsigned char byte_16 = 0x22;
    unsigned char byte_17 = 0x6a;
    unsigned char byte_18 = 0x28;
    unsigned char byte_19 = 0x05;
    unsigned char byte_20 = 0x23;
    unsigned char byte_21 = 0x6a;
    unsigned char byte_22 = 0x2f;
    unsigned char byte_23 = 0x28;
    unsigned char byte_24 = 0x05;
    unsigned char byte_25 = 0x2d;
    unsigned char byte_26 = 0x6e;
    unsigned char byte_27 = 0x23;
    unsigned char byte_28 = 0x05;
    unsigned char byte_29 = 0x33;
    unsigned char byte_30 = 0x34;
    unsigned char byte_31 = 0x05;
    unsigned char byte_32 = 0x69;
    unsigned char byte_33 = 0x6b;
    unsigned char byte_34 = 0x6b;
    unsigned char byte_35 = 0x68;
    unsigned char byte_36 = 0x6b;
    unsigned char byte_37 = 0x63;
    unsigned char byte_38 = 0x6c;
    unsigned char byte_39 = 0x62;
    unsigned char byte_40 = 0x27;
    
    // Store these bytes in an array for comparison
    unsigned char expected_xor_result[] = {
        byte_1, byte_2, byte_3, byte_4, byte_5, byte_6, byte_7, byte_8,
        byte_9, byte_10, byte_11, byte_12, byte_13, byte_14, byte_15, byte_16,
        byte_17, byte_18, byte_19, byte_20, byte_21, byte_22, byte_23, byte_24,
        byte_25, byte_26, byte_27, byte_28, byte_29, byte_30, byte_31, byte_32,
        byte_33, byte_34, byte_35, byte_36, byte_37, byte_38, byte_39, byte_40
    };

    // Check if the XOR result matches the expected result using memcmp
    if (memcmp(encrypted_input, expected_xor_result, len_input) == 0) {
        printf("Correct second flag! You are a Reverse Engineering master! :D\n");
    } else {
        printf("Incorrect second flag, sorry :(\n");
        printf("See you next time. Quitting...\n");
        return 0;
    }

    // Now for the third flag
    printf("So can you give me the third flag? Please? :3\n");
    scanf("%99s", input);

    unsigned char decrypted_flag[FLAG_SIZE];  // Store decrypted flag

    // Decrypt the correct encrypted flag. (vuln) 
    decrypt_flag(encrypted_flag, decrypted_flag);

    // Compare the user input with the decrypted flag
    if (strncmp(input, (char *)decrypted_flag, FLAG_SIZE) == 0) {
        printf("Correct third flag! You are a Reverse Engineering master! :D\n");
    } else {
        printf("Incorrect third flag, sorry :(\n");
        printf("See you next time. Quitting...\n");
    }

    return 0;
}

