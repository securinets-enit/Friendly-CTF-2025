package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	questions := []string{
		"When did this revolt start?",
		"When did this revolt end?",
		"What is the first name of the Palestinian leader that escaped after being issued a warrant for his arrest? Case-Sensitive",
		"What is the first name of the Palestinian feminist activist woman that led an important women's organization? Case-Sensitive",
		"What is the name of the Zionist militia that gained experience with this revolt and practiced their killing as they wished? Format Xxxxxxx",
	}

	answers := []string{
		"1936",
		"1939",
		"Amin",
		"Tarab",
		"Haganah",
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
