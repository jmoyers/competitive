// Given two non-negative integers num1 and num2 represented as string, return
// the sum of num1 and num2.
//
// Note:
//
//     The length of both num1 and num2 is < 5100.
//     Both num1 and num2 contains only digits 0-9.
//     Both num1 and num2 does not contain any leading zero.
//     You must not use any built-in BigInteger library or convert the inputs to
//     integer directly.

const addStrings = (num1, num2) => {
  // do addition via places method
  // start at the end of the string, grab each digit
  // loop until at the highest place, maintaining carry

  let carry = 0;
  let sum = "";

  let i = num1.length - 1;
  let j = num2.length - 1;

  while (i >= 0 || j >= 0) {
    let d1, d2;

    if (i >= 0) d1 = num1.charCodeAt(i) - 48;
    else d1 = 0;

    if (j >= 0) d2 = num2.charCodeAt(j) - 48;
    else d2 = 0;

    let s = d1 + d2 + carry;

    if (s > 9) {
      carry = 1;
      s = s - 10;
    } else {
      carry = 0;
    }

    sum = s + sum;

    j--;
    i--;
  }

  if (carry === 1) sum = "1" + sum;

  return sum;
};

console.log(addStrings("1", "9"));
console.log(12312312 + 23423423);
