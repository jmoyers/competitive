/**
 * @param {number[][]} students
 * @param {number[][]} mentors
 * @return {number}
 */
var maxCompatibilitySum = function (students, mentors) {
  let max = -Infinity;
  const n = students.length;

  const comp = {};

  for (const [i, s] of students.entries()) {
    for (const [j, m] of mentors.entries()) {
      const key = `${i},${j}`;
      comp[key] = s.reduce((sum, v, i) => {
        sum += v === m[i] ? 1 : 0;
        return sum;
      }, 0);
    }
  }

  const explore = (path, mentors) => {
    if (path.length === n) {
      const sum = path.reduce((sum, key) => sum + comp[key], 0);
      max = Math.max(sum, max);
      //console.log(path);
      return;
    }

    let student = path.length;

    for (let i = 0; i < n; i++) {
      if (!mentors[i]) continue;
      path.push(`${student},${i}`);
      mentors[i] = false;
      explore(path, mentors);
      mentors[i] = true;
      path.pop();
    }
  };

  explore([], new Array(n).fill(true));

  return max;
};
