/**
 * @param {string} s
 * @return {string}
 */
const sortString = (s) => {
  const char = (c) => String.fromCharCode(c);
  const code_to_string = (s) =>
    s.map((charCode) => String.fromCharCode(charCode)).join("");

  const src = s
    .split("")
    .map((c) => c.charCodeAt(0))
    .sort((a, b) => a - b);

  const res = [];

  res.push(src.shift());

  let direction = "asc";

  let index = 0;

  while (src.length) {
    index = src.lastIndexOf(res[res.length - 1]) + 1;

    // phase 1
    while (direction === "asc" && res[res.length - 1] < src[index]) {
      res.push(src[index]);
      src.splice(index, 1);

      while (index < src.length && res[res.length - 1] === src[index]) {
        index++;
      }
    }

    if (!src.length) break;

    direction = "desc";
    res.push(src.pop());

    index = src.indexOf(res[res.length - 1]) - 1;
    index = index === -2 ? src.length - 1 : index;

    // phase 2
    while (
      direction === "desc" &&
      index >= 0 &&
      res[res.length - 1] > src[index]
    ) {
      res.push(src[index]);
      src.splice(index, 1);
      index--;
      while (index >= 0 && res[res.length - 1] === src[index]) {
        index--;
      }
    }

    if (!src.length) break;

    direction = "asc";
    res.push(src.shift());
  }

  return code_to_string(res);
};
