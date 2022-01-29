class Solution {
  pair<int,int> getHourMin(string &tp) {
    auto delim = tp.find(':');
    return make_pair(stoi(tp.substr(0, delim)), stoi(tp.substr(delim + 1)));
  }
  void debug(pair<int, int> &t) {
    cout << t.first << ":" << t.second << endl;
  }
  void debug_sort(vector<pair<int,int>> &times) {
    for (auto &p : times)
      debug(p);
  }
  int diff(pair<int, int>& t1, pair<int, int>& t2) {    
    int m1 = (t1.first * 60) + t1.second;    
    
    int m2 = (t2.first * 60) + t2.second;
    int m2_alt = 24 * 60 - m2;    
  
    return min(m2 - m1, m2_alt + m1);
  }
public:
  int findMinDifference(vector<string>& timePoints) {
    vector<pair<int,int>> times;
    
    for (auto &tp : timePoints) {
      times.emplace_back(getHourMin(tp));      
    }
    
    stable_sort(times.begin(), times.end(), [](auto& a, auto& b){
      return a.second < b.second;
    });
    
    stable_sort(times.begin(), times.end());
    
    int min_diff = INT_MAX;
    
    for (int i = 0; i < times.size() - 1; i++) {
      min_diff = min(min_diff, diff(times[i], times[i+1]));
    }
    
    min_diff = min(min_diff, diff(times[0], times[times.size() - 1]));
    
    return min_diff;
  }
};
