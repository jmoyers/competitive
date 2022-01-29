#include <iostream>
#include <utility>
#include <vector>

using namespace std;

class Solution {
  vector<vector<char>> b;
  int rows, cols;
 public:
  vector<vector<char>> updateBoard(vector<vector<char>>& board,
                                   vector<int>& click) {

    if (board.size() == 0 or board[0].size() == 0) {
      return board;
    }

    b = board;

    rows = board.size();
    cols = board[0].size();
    int r = click[0], c = click[1];

    if (board[r][c] == 'M') {
      b[r][c] = 'X';
      return b;
    }

    _updateBoard(r, c);

    return b;
  }

  bool in_board(int r, int c) {
    return r >= 0 and r < b.size() and c >= 0 and c < b[0].size();
  }

  void _updateBoard(int r, int c) {
    if (!in_board(r, c)) return;
    if (b[r][c] != 'E') return;

    vector<pair<int, int>> mines;
    vector<pair<int, int>> empties;

    check_neighbors(r, c, mines, empties);

    if (!mines.empty()) {
      b[r][c] = '0' + mines.size();
    } else {
      b[r][c] = 'B';

      for (auto& e : empties) {
        _updateBoard(e.first, e.second);
      }
    }
  }

  void check_neighbors(int r, int c,
                       vector<pair<int, int>>& mines,
                       vector<pair<int, int>>& empties) {

    vector<pair<int, int>> dirs;

    for (int i = -1; i <= 1; i++)
      for (int j = -1; j <= 1; j++)
        dirs.push_back(make_pair(r + i, c + j));

    for (auto &d : dirs) {
      if (!in_board(d.first, d.second)) continue;
      if (b[d.first][d.second] == 'M') mines.push_back(d);
      if (b[d.first][d.second] == 'E') empties.push_back(d);
    }
  }
};

int main() {
  vector<vector<char>> board = {{'E', 'E', 'E', 'E', 'E'},
                                {'E', 'E', 'M', 'E', 'E'},
                                {'E', 'E', 'E', 'E', 'E'},
                                {'E', 'E', 'E', 'E', 'E'}};
  vector<int> pos = {3, 0};

  auto s = Solution();
  auto result_board = s.updateBoard(board, pos);
  cout << endl << endl;
  for (size_t i = 0; i < result_board.size(); i++) {
    for (size_t j = 0; j < result_board[0].size(); j++) {
      cout << result_board[i][j] << " ";
    }
    cout << endl;
  }
  return 0;
}
