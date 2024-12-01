package main

import (
	"os"
	"bufio"
	"strings"
	"fmt"
	"strconv"
	"math"
)

func readInput(path string) ([]int, []int) {
	file, ferr := os.Open(path)
	defer file.Close()
	if ferr != nil {
		panic(ferr)
	}
	scanner := bufio.NewScanner(file)
	var list1, list2 []int
	for scanner.Scan() {
		lineFields := strings.Fields(scanner.Text())
		numLeft, errLeft := strconv.Atoi(lineFields[0])
		if errLeft != nil {
			panic(errLeft)
		}
		numRight, errRight := strconv.Atoi(lineFields[1])
		if errRight != nil {
			panic(errRight)
		}
		list1 = append(list1, numLeft)
		list2 = append(list2, numRight)
	}
	return list1, list2
}

func mergeSort(arr []int) []int {
	// Base case
	if len(arr) < 2 {
		return arr
	}
	// Complex case (top-down)
	split := len(arr) / 2
	left := mergeSort(arr[:split])
	right := mergeSort(arr[split:])
	// Merge
	ret := []int{}
	L, R := 0, 0
	for L < len(left) && R < len(right) {
		if left[L] < right[R] {
			ret = append(ret, left[L])
			L += 1
		} else {
			ret = append(ret, right[R])
			R += 1
		}
	}
	for L < len(left) {
		  ret = append(ret, left[L])
		  L += 1
	}
	for R < len(right) {
		  ret = append(ret, right[R])
		  R += 1
	}
	return ret
}

func computeDist(list1, list2 []int) int {
	// both lists must be of the same length
	totalDist := 0
	for i := 0; i < len(list1); i++ {
		totalDist += int(math.Abs(float64(list1[i]) - float64(list2[i])))
	}
	return totalDist
}

func computeFreqMap(list []int) map[int]int {
	ret := make(map[int]int, len(list))
	for _, elem := range list {
		val := 0
		if v, ok := ret[elem]; ok == true {
			val = v
		}
		ret[elem] = val + 1
	}
	return ret
}

func computeSimilarityScore(list1, list2 []int) int {
	freqs := computeFreqMap(list2)
	similarityScore := 0
	for i := 0; i < len(list1); i++ {
		f, ok := freqs[list1[i]]
		if ok == true {
			similarityScore += list1[i] * f
		}
	}
	return similarityScore
}

func Day1() {
	inputPath := "./day1_input.txt"
	// O(n)
	// where n is the length of the file
	list1, list2 := readInput(inputPath)
	// O(n*logn)
	list1, list2 = mergeSort(list1), mergeSort(list2)
	// O(n)
	totalDist := computeDist(list1, list2)
	if totalDist != 1660292 {
		panic(fmt.Sprintf("Expected totalDist = 1660292, got %d\n", totalDist))
	}
	fmt.Printf("Total Distance = %d\n", totalDist)
	// O(n) to create the map
	// O(n) to compute similarityScore
	similarityScore := computeSimilarityScore(list1, list2)
	fmt.Printf("Similarity Score = %d\n", similarityScore)
}
