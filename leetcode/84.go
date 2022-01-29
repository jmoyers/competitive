package main

// Given n non-negative integers representing the histogram's bar height where
// the width of each bar is 1, find the area of largest rectangle in the
// histogram.
//
// Above is a histogram where width of each bar is 1, given height =
// [2,1,5,6,2,3].
//
// The largest rectangle is shown in the shaded area, which has area = 10 unit.
//
// Example:
//
// Input: [2,1,5,6,2,3]
// Output: 10

import "fmt"

// the naive implementation would look left and right of every index
// and find where the ceiling of the bars in the histogram drop below
// the current indexes height, then calculate the area
// this is n^2, because for every index, in the worst case you're
// going to look at every other index once

// if we try to iterate once, we can try to keep an invariant whereby
// bars to the left of a given index are less than or equal to the
// index we are examining -- if you think of an upward sloping hill.
// when we find such a peek, we can look backwards until you find
// a bar that is smaller than yourself, and use that as a leftmost
// edge of the rectangle and store a maximum area for that index i.
// once we've examined and found an area for that index, we can
// remove that from the list of indexes to process because being the
// tallest bar we've encountered so far, it will not be a rightmost
// edge of a rectangle for the bars previous to it
//
// because at any given time we're only examining the rightmost item
// in this array representing the "upward slope" we identified before,
// we can use a stack and remove the index from the stack once we've
// classified its area
//
// once we've found the area for a given peak, we go foward to find
// the next peak in the dataset and again work backwards to find the
// next index which has a height smaller than the index we're currently
// examining.
//
// in this way we remove the "tallest" rectangles first, and work outwards
// from these peeks, with the lowest, widest rectangles being examined last
// because we're only iterating through the list once, with a lookbehind
// that only extends as far as the next unprocessed index lower than the current
// indexes
func largestRectangleArea(hist []int) int {
	maxArea := 0

	stack := make([]int, 0)

	// this will force the last ascending set to get processed without
	// having a second loop
	hist = append(hist, 0)

	for i := 0; i < len(hist); i++ {
		if len(stack) == 0 || hist[i] > hist[peek(stack)] {
			stack = append(stack, i)
		} else {
			for len(stack) > 0 && hist[i] < hist[peek(stack)] {
				// we continuously pop til we find something smaller than
				// what we're examining at i, then use that to calculate
				// the width of the rectangle
				// IMPORANT: i does not change here,
				// so as long as we find something larger
				// than the current element being examined at
				// the top of the stack, the "width" of the rectangle
				// formed keeps growing by one
				curr := stack[len(stack)-1]
				stack = stack[:len(stack)-1]
				currHeight := hist[curr]

				// its important to understand i - peek(stack) - 1
				// basically if a bar with a higher height was processed
				// earlier, we want to include that in the width of a shorter
				// rectangle, so we're using the stack the top of the stack
				// to find the leftmost edge of the maximal rectangle at this
				// point. you have to noodle on this part for a while
				area := currHeight * (i - peek(stack) - 1)
				maxArea = max(maxArea, area)
			}

			stack = append(stack, i)
		}
	}

	return maxArea
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func peek(stack []int) int {
	if len(stack) > 0 {
		return stack[len(stack)-1]
	}
	return -1
}

func main() {
	result := largestRectangleArea([]int{2, 1, 5, 6, 2, 3})
	//result := largestRectangleArea([]int{2, 1, 2})
	fmt.Println(result)
}
