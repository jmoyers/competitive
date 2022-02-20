/**
 * @param {number[][]} intervals
 * @return {number}
 */
const minMeetingRooms = (intervals) => {
  // sort the array
  // turn each interval into two events, one is start, one is end
  // iterate over the new events array
  // every time we encounter a start -- increment the value of rooms required
  // every time we encounter any end -- decrement the rooms required
  // O(n * log(n))
  
  const events = [];
  
  for (const i of intervals) {
    events.push({type:'start', time: i[0]});
    events.push({type:'end', time: i[1]});
  }
  
  events.sort((a, b) => {
    const n = a.time - b.time;
    
    if (n === 0) {
      if (a.type === "end") {
        return -1;
      } else {
        return 1;
      }
    }
    
    return n;
  });
  
  let max = 0, rooms = 0;
  
  for (const e of events) {
    if (e.type === "start") {
      rooms += 1;
      max = Math.max(rooms, max);
    } else {
      rooms -= 1;
    }
  }
  
  return max;
};
