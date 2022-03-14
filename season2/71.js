/**
 * @param {string} path
 * @return {string}
 */
var simplifyPath = function (path) {
  // split /
  // we want to convert an array of sub path expressions
  // to an array of absolute path expressions, remove any empties
  // handle non . or .. period file names

  let parts = path
    .split("/")
    .filter((path) => path.length !== 0 && path !== ".");

  // ~/some/path/and/here

  // handle ..
  const ans = [];

  for (let i = 0; i < parts.length; i++) {
    if (parts[i] === "..") {
      if (ans.length) ans.pop();
    } else {
      ans.push(parts[i]);
    }
  }

  return "/" + ans.join("/");
};
