class Solution {
public:
  bool isRobotBounded(string instructions) {
    // make sure each individual direction vector is 0
    // calculate the 4-directional vector for the entire string by parsing
    // when we see a g, we increment the direction we're currently on by one
    // if all direction vectors are not 0 by the end, there is no circle
    array<int, 4> dir_vectors {0,0,0,0};
    int dir = 0;
    // 0 - north
    // 1 - east
    // 2 - south
    // 3 - west
    // these will wrap, for instance, LLLL will wrap back north
    // L = -1
    // R = +1
    // if we go out of bounds, we wrap
    
    // repeat 4 times in case we have an instruction which will make a loop after 4 cycles
    // like GL, or GR etc
    for (int i = 0; i < 4; i++) {
      for (auto& c : instructions) {
        if (c == 'G') {
          dir_vectors[dir] += 1;
        } else if (c == 'L') {
          dir -= 1;
        } else if (c == 'R') {
          dir += 1;
        }

        if (dir > 3) {
          dir = 0;
        } else if (dir < 0) {
          dir = 3;
        }
      }  
    }
    
    // north/south vecotrs need to cancel
    // west/east vectors need to cancel    
    return (dir_vectors[0] - dir_vectors[2] == 0) and (dir_vectors[1] - dir_vectors[3] == 0);
  }
};
