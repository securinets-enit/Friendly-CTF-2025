#include <iostream>
#include <fstream>
#include <vector>

int main() {
    std::ifstream inputFile("output", std::ios::in);
    if (!inputFile.is_open()) {
        std::cerr << "Error: Could not open output" << std::endl;
        return 1;
    }

   
    std::vector<char> buffer((std::istreambuf_iterator<char>(inputFile)),
                             std::istreambuf_iterator<char>());
    inputFile.close();

    if (buffer.empty()) {
        std::cerr << "Error: File is empty." << std::endl;
        return 1;
    }

    std::ofstream outputFile("decoded_flag.txt", std::ios::out);
    if (!outputFile.is_open()) {
        std::cerr << "Error: Could not open decoded_flag.txt" << std::endl;
        return 1;
    }

    size_t start = 0;
    size_t end = 0;
    bool foundBraces = false;

    
    for (size_t i = 0; i < buffer.size(); ++i) {
        if (buffer[i] == '{' && !foundBraces) {
            start = i;
            foundBraces = true;
        } else if (buffer[i] == '}' && foundBraces) {
            end = i;
            break;
        }
    }

    if (!foundBraces || end <= start) {
        std::cerr << "Error: Braces not found properly." << std::endl;
        return 1;
    }

    
    outputFile.write(buffer.data(), start + 1);

    
    for (size_t i = start + 1; i < end; ++i) {
        char ch = buffer[i];
        
        char originalChar = (i % 2 == 0) ? ch - 5 : ch + 2;
        outputFile.put(originalChar);
    }

    
    outputFile.write(buffer.data() + end, buffer.size() - end);

    outputFile.close();
    std::cout << "Decoding completed. Check decoded_flag.txt" << std::endl;

    return 0;
}
