// You are given coins of different denominations and a total amount of money
// amount. Write a function to compute the fewest number of coins that you need
// to make up that amount. If that amount of money cannot be made up by any
// combination of the coins, return -1.
//
// Example 1:
//
// Input: coins = [1, 2, 5], amount = 11
// Output: 3
// Explanation: 11 = 5 + 5 + 1
//
// Example 2:
//
// Input: coins = [2], amount = 3
// Output: -1
//
// Note:
// You may assume that you have an infinite number of each kind of coin.

const coinChange = (coins, amount) => {
  // since you aren't given a 1 coin always, this is not straightforward
  // modulus. looks like a bin packing problem where you need to use memoization.
  // the naive solution is just to start with the largest coin, divide into
  // the amount, and use the modulus as remainder.
  //
  // however, i can imagine no 1 coin, but an odd value coin that could make up
  // for the lack of a 1 coin with multiples of a middle denomination.
  // e.g. 1, 5, 6, 8, amount = 11 -- 5, 6 is the answer here, but 8 goes into 11
  //
  // so, if we break this into smaller sub problems and solve from bottom up
  // we need to build a table of the minimum number of coins for each value
  // leading up to {amount}. this can be a 1 dimensional array, assuming we dont
  // need to actually say the denomination of the coins used.
  //
  // it needs to be a 2 dimensional array if you want to work backwards through the
  // table to find the actual denominations used

  // O(n * amount), where n is denominations
  // space is a table of {amount}

  // store minimum number of coins required for each amount
  // we'll use the max safe integer as an invalid value - if we encounter max safe
  // integer in the final solution, we know the amount was not solvable
  const minCoins = new Array(amount + 1);
  minCoins.fill(Number.MAX_SAFE_INTEGER);

  // 0th slot is 0 amount, so 0 coins is the answer, always
  minCoins[0] = 0;

  // loop through every sub-amount and solve minimum number of coins
  // start at 1 because we've solved 0 already - invariant
  for (let i = 1; i < amount + 1; i++) {
    // for each denomination, if you can use this coin (if the amount is larger or =)
    // subtract that from the current amount, and then try to find the solution
    // for the remainder in the memoized table from previously solved subproblems
    for (let j = 0; j < coins.length; j++) {
      // if this coin is smaller than current amount, we can check if its
      // part of the optimal solution
      if (coins[j] <= i) {
        // 1 = adding one of this coin
        // so we go back in the table (i - coins[j]) to check whether we've
        // been able to solve the subproblem of the amount left over after
        // taking this coin already. if this is less than the current # of
        // coins already stored in the table, we've found a new minimum for
        // this subproblem
        minCoins[i] = Math.min(minCoins[i], 1 + minCoins[i - coins[j]]);
      }
    }
  }

  return minCoins[amount] === Number.MAX_SAFE_INTEGER ? -1 : minCoins[amount];
};

let r = coinChange([1, 2, 5], 11);
console.log(r);
// Output: 3
