/**
 * @param {string} text
 * @param {string} first
 * @param {string} second
 * @return {string[]}
 */
const findOcurrences = (text, first, second) => {
  const words = text.split(" ");
  let ans = [];

  for (const [i, word] of words.entries()) {
    if (i >= 2 && words[i - 2] === first && words[i - 1] === second) {
      ans.push(word);
    }
  }

  return ans;
};
