/**
 * @param {string} s
 * @return {number}
 */
var secondHighest = function (s) {
  if (s.length < 2) return -1;

  const digits = new Set(
    s
      .split("")
      .filter((c) => c.charCodeAt(0) >= 48 && c.charCodeAt(0) <= 57)
      .map((n) => Number(n))
      .sort((a, b) => b - a)
  );

  if (digits.size < 2) return -1;

  return Array.from(digits)[1];
};
