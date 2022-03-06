/**
 * @param {string} s
 * @param {number[]} shifts
 * @return {string}
 */
const shiftingLetters = (s, shifts) => {
  const prefix = new Array(shifts.length);

  shifts.reverse().reduce((sum, n, i) => {
    prefix[i] = sum + n;
    return prefix[i];
  }, 0);

  const ord = s.split("").map((c) => c.charCodeAt(0) - 97);

  //console.log(prefix, ord);

  for (const [i, shift] of prefix.reverse().entries()) {
    ord[i] = (ord[i] + shift) % 26;
  }

  //console.log(ord);

  return ord.map((charCode) => String.fromCharCode(charCode + 97)).join("");
};
