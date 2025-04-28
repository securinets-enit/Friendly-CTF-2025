package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	questions := []string{
		"What is this specific place? Format: xx-xxxxx xxxx",
		"In what year did this stealing attempt happen?",
		"What was the name of the mentioned commission? Format xxxx (Case-Sensitive)",
	}

	answers := []string{
		"Al-Buraq wall",
		"1929",
		"Shaw",
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
