#include <iostream>
#include <fstream>
#include <vector>

int main() {
    std::ifstream flagFile("flag.txt", std::ios::in);
    std::ofstream outputFile("output", std::ios::app);
    
    if (!flagFile.is_open()) {
        std::cout << "[+] No flag found..." << std::endl;
        return 1;
    }
    
    if (!outputFile.is_open()) {
        std::cout << "[+] Please run this on the server" << std::endl;
        return 1;
    }

    
    std::string content((std::istreambuf_iterator<char>(flagFile)),
                        (std::istreambuf_iterator<char>()));

    size_t start = content.find('{');
    size_t end = content.find('}');

    if (start == std::string::npos || end == std::string::npos || start >= end) {
        std::cout << "[+] No braces found in the flag" << std::endl;
        return 1;
    }

    
    outputFile.write(content.c_str(), start + 1); 
   for (size_t i = start + 1; i < end; i++) {
        char ch = content[i];
        char transformedChar = (i % 2 == 0) ? ch + 5 : ch - 2;
        outputFile.put(transformedChar);
    }

    
    outputFile.write(content.c_str() + end, content.size() - end);

    outputFile.close();
    flagFile.close();
    
    return 0;
}
