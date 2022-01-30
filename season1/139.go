package main

import "fmt"

func wordBreak(s string, words []string) bool {
	// this is a tabular approach to dynamic programming rather than recursive,
	// but its the same idea
	//
	// this array will contain the answer to the sub-problem is this string
	// breakable up to the ith character therefore at the end, when we return
	// memo[len(s)] it will contain the answer to whether the entire string is
	// breakable
	//
	// we do this because to get the answer, we have to compute the answer to the
	// ith character potentially many times for strings with repeated prefixes etc
	memo := make([]bool, len(s)+1)

	// the base case of an empty string must be breakable
	memo[0] = true

	// create a map of words for O(1) lookup when we want to check if a given
	// substring is in the set of words given to us
	wordMap := make(map[string]bool)

	for _, w := range words {
		wordMap[w] = true
	}

	// check for each position i if the substring can be split such that 0 -> j is
	// breakable (prev calculated and stored as memo[j]) and the remainder of the
	// string from j -> i is a word in the list given to us. in this case, 0 -> i
	// is also breakable. this loops first execution is contingent upon the 'base
	// case' of an empty string being breakable (memo[0] = true)
	//
	// each iteration of the outer loop adds one more character to the set
	// being examined. each iteration of the inner loop partitions the set
	// at a different point to determine if that split creates a word +
	// a substring that has previously been identified as a breakable string
	// and so therefore also contains all words
	//
	// this starts at 1 because 0 is the base case and is defined above
	for i := 1; i <= len(s); i++ {
		for j := i - 1; j >= 0; j-- {
			if memo[j] && wordMap[s[j:i]] {
				memo[i] = true
				break
			}
		}
	}

	return memo[len(s)]
}

func main() {
	result := wordBreak("catsanddogs", []string{"cats", "and", "dogs"})
	fmt.Println(result)
}
