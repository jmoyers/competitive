// Given an array of words and a width maxWidth, format the text such that each
// line has exactly maxWidth characters and is fully (left and right) justified.
//
// You should pack your words in a greedy approach; that is, pack as many words
// as you can in each line. Pad extra spaces ' ' when necessary so that each
// line has exactly maxWidth characters.
//
// Extra spaces between words should be distributed as evenly as possible. If
// the number of spaces on a line do not divide evenly between words, the empty
// slots on the left will be assigned more spaces than the slots on the right.
//
// For the last line of text, it should be left justified and no extra space is
// inserted between words.
//
// Note:
//
//     A word is defined as a character sequence consisting of non-space characters only.
//     Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
//     The input array words contains at least one word.
//
// Example 1:
//
// Input:
// words = ["This", "is", "an", "example", "of", "text", "justification."]
// maxWidth = 16
// Output:
// [
//    "This    is    an",
//    "example  of text",
//    "justification.  "
// ]
//
// Example 2:
//
// Input:
// words = ["What","must","be","acknowledgment","shall","be"]
// maxWidth = 16
// Output:
// [
//   "What   must   be",
//   "acknowledgment  ",
//   "shall be        "
// ]
// Explanation: Note that the last line is "shall be " instead of "shall be",
// because the last line must be left-justified instead of fully-justified. Note
// that the second line is also left-justified becase it contains only one word.
//
// Example 3:
//
// Input:
// words = ["Science","is","what","we","understand","well","enough","to","explain",
//          "to","a","computer.","Art","is","everything","else","we","do"]
// maxWidth = 20
// Output:
// [
//   "Science  is  what we",
//   "understand      well",
//   "enough to explain to",
//   "a  computer.  Art is",
//   "everything  else  we",
//   "do                  "
// ]
//

const fullJustify = (words, maxWidth) => {
  const lines = [];

  // pack a line based on max width dequeue words from the front of the array
  // see if it will fit inside the current line with a space + word length
  //
  // when no more will fit, we take a look at the whitespace count and divide by
  // the number of words + 1 to get the number of spaces between words
  let currLine = "";
  let wordIndex = 0;

  while (wordIndex < words.length) {
    const wordsForLine = [];
    let lineLength = 0;
    let lineDone = false;

    while (!lineDone && wordIndex < words.length) {
      const word = words[wordIndex];

      if (lineLength + word.length <= maxWidth) {
        wordsForLine.push(word);
        lineLength += word.length + 1;
        wordIndex++;
      } else {
        lineDone = true;
      }
    }

    // count total number of available spaces by subtracting the
    // total available width (maxWidth) by the total word length
    // then we need a generall even number of spaces between words
    //
    // we need to handle a special case where the number of spaces
    // does not go into the intervals between words evenly. if this
    // is the case, we add one to the number of spaces available and
    // then manually handle the last word, which will have one less
    // space prepended to it
    //
    // other edge cases:
    // single word lines -- add spaces equivalent to the leftover
    //   line length to the end of the line string
    // last line -- can be more than one word, but we still only
    //   use one space between words and send the rest of the extra
    //   spaces to after
    const lengthOfWords = wordsForLine.reduce(
      (acc, word) => acc + word.length,
      0
    );

    let spaces = maxWidth - lengthOfWords;

    const intervals = wordsForLine.length - 1;

    let spaceString = "";
    let line = "";

    const leftover = spaces % intervals;

    if (leftover > 0 && wordIndex < words.length) {
      spaces += 1;
    }

    let spaceCount = Math.ceil(spaces / intervals);

    if (intervals !== 0 && words.length !== wordIndex) {
      if (leftover === 0) {
        // default case - spaces go into intervals evenly
        spaceString = " ".repeat(spaceCount);
        line = wordsForLine.join(spaceString);
      } else {
        // spaces don't go into intervals evenly, so we need
        // one less space for a number of words equal to the
        // leftover

        line = wordsForLine
          .map((word, index) => {
            // last word
            if (index === wordsForLine.length - 1) return word;
            // the first {leftover} words have one extra space
            if (index > leftover - 1) return word + " ".repeat(spaceCount - 1);
            return word + " ".repeat(spaceCount);
          })
          .join("");
      }
    } else {
      // single word lines and last line
      if (wordsForLine.length === 1) spaceString = " ".repeat(spaces);
      else if (spaces - wordsForLine.length > 0)
        spaceString = " ".repeat(spaces - wordsForLine.length + 1);
      else spaceString = "";
      line = wordsForLine.join(" ") + spaceString;
    }

    lines.push(line);
  }

  return lines;
};

// const res = fullJustify(
//   [
//     "Science",
//     "is",
//     "what",
//     "we",
//     "understand",
//     "well",
//     "enough",
//     "to",
//     "explain",
//     "to",
//     "a",
//     "computer.",
//     "Art",
//     "is",
//     "everything",
//     "else",
//     "we",
//     "do",
//   ],
//   20
// );

// const res = fullJustify(
//   ["What", "must", "be", "acknowledgment", "shall", "be"],
//   16
// );

// const res = fullJustify(
//   ["This", "is", "an", "example", "of", "text", "justification."],
//   16
// );

// const res = fullJustify(
//   [
//     "ask",
//     "not",
//     "what",
//     "your",
//     "country",
//     "can",
//     "do",
//     "for",
//     "you",
//     "ask",
//     "what",
//     "you",
//     "can",
//     "do",
//     "for",
//     "your",
//     "country",
//   ],
//   16
// );

// const res = fullJustify(
//   [
//     "My",
//     "momma",
//     "always",
//     "said,",
//     '"Life',
//     "was",
//     "like",
//     "a",
//     "box",
//     "of",
//     "chocolates.",
//     "You",
//     "never",
//     "know",
//     "what",
//     "you're",
//     "gonna",
//     "get.",
//   ],
//   20
// );

const res = fullJustify(
  [
    "Do",
    "all",
    "the",
    "good",
    "you",
    "can,",
    "By",
    "all",
    "the",
    "means",
    "you",
    "can,",
    "In",
    "all",
    "the",
    "ways",
    "you",
    "can,",
    "In",
    "all",
    "the",
    "places",
    "you",
    "can,",
    "At",
    "all",
    "the",
    "times",
    "you",
    "can,",
    "To",
    "all",
    "the",
    "people",
    "you",
    "can,",
    "As",
    "long",
    "as",
    "ever",
    "you",
    "can.",
  ],
  26
);

res.forEach((line) => console.log("| " + line + " |"));
