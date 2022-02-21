/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
const canCompleteCircuit = (gas, cost) => {
  // because we're guaranteed to have one solution
  // if we check if the total gas surplus for a whole loop is at least 0,
  // we can guarantee there is one trip
  // we should be able to start anywhere and anytime we run out of gas along
  // the way, we should be able to assume the starting point is our current index + 1
  // if it exists, once the loop is done and our surplus is above zero, we can return the
  // starting point that we found during our first iteration
  
  let tank = 0, start = 0, surplus = 0;
  
  
  for (let i = 0; i < gas.length; i++) {
    const net = gas[i] - cost[i]
    tank += net;
    surplus += net;
    
    //console.log(tank, net, i)
    
    if (tank < 0) {
      //console.log('ran out of gas')
      start = i + 1;
      tank = 0;
    }
  }
  
  return surplus >= 0 ? start : -1;
};
