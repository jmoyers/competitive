// In an alien language, surprisingly they also use english lowercase letters,
// but possibly in a different order. The order of the alphabet is some
// permutation of lowercase letters.
//
// Given a sequence of words written in the alien language, and the order of the
// alphabet, return true if and only if the given words are sorted
// lexicographicaly in this alien language.
//
// Example 1:
//
// Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
// Output: true
// Explanation: As 'h' comes before 'l' in this language, then the sequence is
// sorted.
//
// Example 2:
//
// Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
// Output: false
// Explanation: As 'd' comes after 'l' in this language, then words[0] >
// words[1], hence the sequence is unsorted.
//
// Example 3:
//
// Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
// Output: false
// Explanation: The first three characters "app" match, and the second string is
// shorter (in size.) According to lexicographical rules "apple" > "app",
// because 'l' > '∅', where '∅' is defined as the blank character which is less
// than any other character (More info).
//
// Constraints:
//
//     1 <= words.length <= 100
//     1 <= words[i].length <= 20
//     order.length == 26
//     All characters in words[i] and order are English lowercase letters.

const isAlienSorted = (words, order) => {
  // create a character map with a value that signifies its order
  let charMap = {};
  for (let i = 0; i < order.length; i++) {
    charMap[order[i]] = i;
  }
  // first letter of each word she follow the given order
  let lastWord = false;

  for (const word of words) {
    if (lastWord && charMap[word[0]] < charMap[lastWord[0]]) {
      return false;
    }

    // identify prefixes in words that are next to each other
    let y = 0;
    let j = 0;

    while (lastWord && lastWord[y] === word[j]) {
      y++;
      j++;
    }

    if (y > 0 && j === word.length && word.length < lastWord.length) {
      // if we word has same prefix but is longer, should be later
      return false;
    }

    if (y > 0 && charMap[word[j]] < charMap[lastWord[y]]) {
      // the first letter after the prefix should follow the order
      return false;
    }

    lastWord = word;
  }

  return true;
};

//let r = isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz");
//console.log(r);
// Output: true
// Explanation: As 'h' comes before 'l' in this language, then the sequence is
// sorted.

//let r = isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz");
//console.log(r);
// Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
// Output: false

//let r = isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz");
//console.log(r);
// Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
// Output: false
// Explanation: As 'd' comes after 'l' in this language, then words[0] >
// words[1], hence the sequence is unsorted.
//let r = isAlienSorted(["apap", "app"], "abcdefghijklmnopqrstuvwxyz");
//console.log(r);
