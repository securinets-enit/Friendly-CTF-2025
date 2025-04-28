package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	questions := []string{
		"What is the empire that was defeated by the british power in WW1 to take control of palestine?",
		"There was a secret treaty between France and the UK in which they agreed on how to divide the middle east following up the war. What is the name of the agreement? Case-Sensitive",
		"In which year was it?",
		"Just a year after, there was a famous declaration in which the British declared its aim to establish “a national home for the Jewish people” in Palestine. What was the family name of the Sender of this letter? Case-sensitive",
		"What was the family name of the receiver? Case-sensitive",
	}

	answers := []string{
		"Ottoman",
		"Sykes-Picot", // normal dash
		"1916",
		"Balfour",
		"Rothschild",
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

	// If all answers are correct, read flag.txt
	flag, err := os.ReadFile("flag.txt")
	if err != nil {
		fmt.Println("Error reading flag.txt:", err)
		return
	}

	fmt.Println("\nCongratulations! Here's your flag:")
	fmt.Println(string(flag))
}
