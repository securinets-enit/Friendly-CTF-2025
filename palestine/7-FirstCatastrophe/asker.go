package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	questions := []string{
		"What was this tragic displacement event known as?",
		"What is the most notable Zionist militia that was responsible for many of the genocide and cleansing that happened?",
		"In which year did the first phase of this war start?",
		"In which month?",
		"Was there any \"external\" countries involved in the first phase?",
		"In which year did the second phase of this start?",
		"In which month?",
		"Was there any \"external\" countries involved directly with their armies?",
		"How many?",
		"In which year did it end?",
		"In which month?",
	}

	answers := []string{
		"Nakba",
		"Haganah",
		"1947",
		"November",
		"No",
		"1948",
		"May",
		"Yes",
		"5",
		"1949",
		"January",
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
