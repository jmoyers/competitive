/**
 * @param {number} n
 * @return {number}
 */
const countOrders = (n) => {
  let ans = 1,
    modulo = Math.pow(10, 9) + 7;

  for (let i = 1; i <= n; i++) {
    // number of possible pickup permutations
    ans *= i;
    ans %= modulo;
    // number of possible delivery locations -- https://www.youtube.com/watch?v=H0Yl1AlUuK8
    // essentially building up from placing a single delivery after a single pickup
    // you add 2 locations for the delivery every time the # of deliveries go up by one
    ans *= 2 * i - 1;
    ans %= modulo;
  }

  return ans % modulo;
};
