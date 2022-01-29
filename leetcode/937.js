const reorderLogFiles = logs => {
  logs = logs.map(l => {
    let space_index = l.indexOf(" ");
    return [l.substr(0, space_index), l.substr(space_index + 1)];
  });

  let alpha = {
    start: "a".charCodeAt(0),
    end: "z".charCodeAt(0)
  };

  const isAlpha = s => {
    return s[1].charCodeAt(0) >= alpha.start && s[1].charCodeAt(0) <= alpha.end;
  };

  let alphaLogs = [];
  let digitLogs = [];

  for (let l of logs) {
    if (isAlpha(l)) alphaLogs.push(l);
    else digitLogs.push(l);
  }

  alphaLogs.sort((a, b) => {
    console.log(a[1], ">", b[1], a[1] > b[1]);
    if (a[1] == b[1]) {
      // in the case of lexographic tie, use the id
      return a[0] > b[0] ? 1 : -1;
    } else {
      return a[1] > b[1] ? 1 : -1;
    }
  });

  logs = [...alphaLogs, ...digitLogs];

  logs = logs.map(l => {
    return l[0] + " " + l[1];
  });

  return logs;
};

reorderLogFiles([
  "dig1 8 1 5 1",
  "let1 art can",
  "dig2 3 6",
  "let2 own kit dig",
  "let3 art zero"
]);
