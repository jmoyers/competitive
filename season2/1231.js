/**
 * @param {number[]} sweetness
 * @param {number} k
 * @return {number}
 */
const maximizeSweetness = (sweetness, k) => {
  let left = Math.min(...sweetness);
  let right = Math.floor(sweetness.reduce((sum, n) => sum + n) / (k + 1));

  while (left < right) {
    // mid is the target sweetness for ourselves, we're checking to see
    // if there is a valid set of cuts that make mid a valid sweetness to give ourselves
    // if we can't successfully create enough pieces of chocolate using this level,
    // our own chocolate potentially needs to get smaller. if we can, we can possibly go bigger,
    // so we try the next mid in the right partition
    const mid = Math.floor((left + right + 1) / 2);

    let curr = 0;
    let assigned = 0;

    for (const s of sweetness) {
      curr += s;

      // we make sure everyone else has bigger or equal chocolate
      if (curr >= mid) {
        assigned += 1;
        curr = 0;
      }

      if (assigned >= k + 1) break;
    }

    if (assigned >= k + 1) {
      // this level of chocolate was workable, but maybe too small
      left = mid;
    } else {
      // this level of chocolate was invalid
      right = mid - 1;
    }
  }

  return left;
};
