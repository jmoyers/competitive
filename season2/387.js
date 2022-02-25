const firstUniqChar = (s) => {
  const freq = s.split("").reduce((o, c) => {
    o[c] = o[c] ? o[c] + 1 : 1;
    return o;
  }, {});

  const non_repeating = new Set(Object.keys(freq).filter((c) => freq[c] === 1));

  for (const [i, c] of s.split("").entries()) {
    if (non_repeating.has(c)) return i;
  }

  return -1;
};
