/**
 * @param {string} columnTitle
 * @return {number}
 
AA 27 - Z = 26 + 1 -> AA = 27
base 26 

AB - (2 * 26^0) + (1 * 26^1)
 */
const titleToNumber = (columnTitle) => {
  let place = 0;
  let total = 0;
  for (const c of columnTitle.split("").reverse()) {
    const char = c.charCodeAt(0) - 64;
    const val = char * Math.pow(26, place);
    //console.log(c, char, place, val);
    total += val;
    place += 1;
  }
  return total;
};
