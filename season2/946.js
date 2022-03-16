/**
 * @param {number[]} pushed
 * @param {number[]} popped
 * @return {boolean}
 */
const validateStackSequences = function (pushed, popped) {
  let push_sim = [];
  let pop_index = 0;

  while (pushed.length) {
    push_sim.push(pushed.shift());

    while (
      push_sim.length &&
      push_sim[push_sim.length - 1] === popped[pop_index]
    ) {
      push_sim.pop();
      pop_index++;
    }
  }

  return pop_index === popped.length;
};
