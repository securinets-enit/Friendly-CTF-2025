package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	questions := []string{
		"What was the name of this commission?",
		"Originally, the commission was meant to be led by 4 countries but ended up being led by only one of them — The US. Three of them are mentioned in the paragraph above. What is the fourth one?",
		"Even though the report was finished by August 1919, it was released only after few years. In what year was the report published?",
	}

	answers := []string{
		"King-Crane",
		"Italy",
		"1922",
	}

	reader := bufio.NewReader(os.Stdin)

	for i := 0; i < len(questions); i++ {
		fmt.Println("---")
		fmt.Printf("Question %d: %s\n", i+1, questions[i])
		for {
			fmt.Print("Answer: ")
			input, err := reader.ReadString('\n')
			if err != nil {
				fmt.Println("Error reading input, try again.")
				continue
			}
			input = strings.TrimSpace(input)

			if input == answers[i] {
				fmt.Println("Correct answer!")
				break
			} else {
				fmt.Println("Incorrect. Try again.")
			}
		}
	}

	flag, err := os.ReadFile("flag.txt")
	if err != nil {
		fmt.Println("Error reading flag.txt:", err)
		return
	}

	fmt.Println("\nCongratulations! Here's your flag:")
	fmt.Println(string(flag))
}
