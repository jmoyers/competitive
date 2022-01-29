// Convert a non-negative integer to its english words representation. Given
// input is guaranteed to be less than 2^31 - 1.
//
// Example 1:
//
// Input: 123
// Output: "One Hundred Twenty Three"
//
// Example 2:
//
// Input: 12345
// Output: "Twelve Thousand Three Hundred Forty Five"
//
// Example 3:
//
// Input: 1234567
// Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty
// Seven"
//
// Example 4:
//
// Input: 1234567891
// Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty
// Seven Thousand Eight Hundred Ninety One"
//

const numberToWords = n => {
  // create a map of english words that map to integers of small
  // sizes, followed by 10s place, 100s place, 1000s place up to
  // a billion
  const word_map = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
    20: "Twenty",
    30: "Thirty",
    40: "Forty",
    50: "Fifty",
    60: "Sixty",
    70: "Seventy",
    80: "Eighty",
    90: "Ninety",
    100: "Hundred",
    1000: "Thousand",
    1000000: "Million",
    1000000000: "Billion"
  };

  const intervals = Object.keys(word_map).map(x => parseInt(x));

  let curr = n;
  let words = [];

  if (curr === 0) return "Zero";

  // from largest interval to smallest
  while (intervals.length && curr > 0) {
    let i = intervals.pop();
    let dividedBy = Math.floor(curr / i);
    let remainder = curr % i;
    if (dividedBy >= 1) {
      // divisible by this interval
      if (curr >= 100) {
        // this is recursive because when you get to the case of 100k
        // it will say "hundred thousand" instead of "one hundred thous.."
        words.push(numberToWords(dividedBy));
      }
      words.push(word_map[i]);
      curr = remainder;
    }
  }

  // side note: javascript numbers go up to 2^53 so we good

  // come up with a loop that runs backwards, once per "place" using
  // division and modulus to deal with identifying the "place" value
  // and modulus for dealing with the remainder

  // join the array together to form the final english compound phrase
  return words.join(" ");
};

console.log(numberToWords(1500026));
