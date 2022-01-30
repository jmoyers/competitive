"""
---
number: 843
title: Guess the Word
difficulty: hard
---
This problem is an interactive problem new to the LeetCode platform.

We are given a word list of unique words, each word is 6 letters long, and
one word in this list is chosen as secret.

You may call master.guess(word) to guess a word. The guessed word should have
type string and must be from the original list with 6 lowercase letters.

This function returns an integer type, representing the number of exact
matches (value and position) of your guess to the secret word. Also, if your
guess is not in the given wordlist, it will return -1 instead.

For each test case, you have 10 guesses to guess the word. At the end of any
number of calls, if you have made 10 or less calls to master.guess and at
least one of these guesses was the secret, you pass the testcase.

Besides the example test case below, there will be 5 additional test cases,
each with 100 words in the word list. The letters of each word in those
testcases were chosen independently at random from 'a' to 'z', such that
every word in the given word lists is unique.

Example 1:
Input: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]

Explanation:

master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
master.guess("abcczz") returns 4, because "abcczz" has 4 matches.

We made 5 calls to master.guess and one of them was the secret, so we pass the test case.
Note:  Any solutions that attempt to circumvent the judge will result in
disqualification.
"""

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:


"""
I'm not gonna implement master, pretty simple though.

First, I thought of a graph with edges based on identical character/index pairs.
Then I thought, maybe there is a simpler idea where we just remove items from
the word list based on information we've found -- if you guess word and it
has 0 in common with the target word, we know any word that has anything in
common with the word we guessed can be safely removed from the list.

We also know that any word that has more in common with the word guessed than
the word we guessed has in common with the target word, we can safely remove 
that word.

We also know that any word which has less in common with our chosen word than
our chosen word has in common with the target can also be safely removed. So,
through math (I'm not sure what kind) we can narrow down our list to 1 within
10 guesses for a word list of 100.
"""

from typing import List
from random import sample
from copy import copy


class Solution:
    def findSecretWord(self, wordlist: List[str], master: "Master") -> None:
        word_set = set(wordlist)

        while True:
            word = sample(word_set, 1)[0]
            val = master.guess(word)

            if val == 6:
                return

            removed = []

            if val == 0:
                for w in word_set:
                    for i in range(6):
                        if w[i] == word[i]:
                            removed.append(w)
                            break
                for w in removed:
                    word_set.remove(w)
                continue

            # up to 100 constant
            for w in word_set:
                match_count = 0
                for i in range(6):
                    if w[i] == word[i]:
                        match_count += 1

                if match_count < val:
                    removed.append(w)

            # o 1
            for w in removed:
                word_set.remove(w)

