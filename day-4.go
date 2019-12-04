package main

import "fmt"
import "strconv"

func main() {
	lower, upper := 130254, 678275
	count := 0
	for i := lower; i <= upper; i++ {
		if valid(i) { count++ }
	}
	fmt.Println("Part One:", count)
}

func valid(num int) bool {
	numString := strconv.Itoa(num)
	adjValues := false
	for i := 0; i < len(numString)-1; i++ {
		num1, _ := strconv.Atoi(string(numString[i]))
		num2, _ := strconv.Atoi(string(numString[i+1]))
		if !(num1 <= num2) { return false }
		if numString[i] == numString[i+1] { adjValues = true }
	}
	return adjValues
}