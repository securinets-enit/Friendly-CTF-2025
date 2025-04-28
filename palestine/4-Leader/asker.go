package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	questions := []string{
		"What is the name of this resistance organization? Format: Xxxxx Xxxx",
		"What is the Family name of this leader? Format Xx-Xxxxxx",
		"In which country was he born? Case-Sensitive",
		"In what year was he born?",
		"In which country did he pass out? Case-Sensitive",
		"In what year did he pass out?",
	}

	answers := []string{
		"Black Hand",
		"Al-Qassam",
		"Syria",
		"1882",
		"Palestine",
		"1935",
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
