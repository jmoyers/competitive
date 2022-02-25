/**
 * @param {string} version1
 * @param {string} version2
 * @return {number}
 */
const compareVersion = (version1, version2) => {
  const v1 = version1.split(".");
  const v2 = version2.split(".");

  for (const [i, v] of v1.entries()) {
    v1[i] = Number(v);
  }

  for (const [i, v] of v2.entries()) {
    v2[i] = Number(v);
  }

  const size = Math.min(v1.length, v2.length);

  for (let i = 0; i < size; i++) {
    if (v1[i] < v2[i]) {
      return -1;
    }
    if (v1[i] > v2[i]) {
      return 1;
    }
  }

  //console.log(v1, v2)

  if (v1.length > v2.length) {
    for (let i = size; i < v1.length; i++) {
      if (v1[i] > 0) return 1;
    }
  } else if (v2.length > v1.length) {
    for (let i = size; i < v2.length; i++) {
      //console.log(v2[i], size, v2.length)
      if (v2[i] > 0) return -1;
    }
  }
  return 0;
};
