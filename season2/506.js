const findRelativeRanks = (score) => {
  const ans = [...score];

  const map = score.reduce((o, s, i) => {
    o[s] = i;
    return o;
  }, {});

  score
    .sort((a, b) => b - a)
    .forEach((n, i) => {
      let placement = "";
      if (i === 0) placement = "Gold Medal";
      else if (i === 1) placement = "Silver Medal";
      else if (i === 2) placement = "Bronze Medal";
      else placement = `${i + 1}`;

      map[n] = placement;
    });

  return ans.map((n) => map[n]);
};
