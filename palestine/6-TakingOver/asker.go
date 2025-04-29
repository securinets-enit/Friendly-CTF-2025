package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	questions := []string{
		"What is the name of this organization?",
		"What is the number of this resolution?",
		"In what year did this resolution adopt?",
		"In which month?",
		"Which day was it?",
		"How many countries were assigned to help establish this?",
		"In which year was the UK ordered to leave the land?",
		"In which month?",
		"In which day?",
		"Did it declare an independent Palestinian state? (Of course not)",
		"Did it declare an official Jewish state? (Of course)",
	}

	answers := []string{
		"United Nations",
		"181",
		"1947",
		"November",
		"29",
		"5",
		"1948",
		"August",
		"1",
		"No",
		"Yes",
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
