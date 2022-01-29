class Logger {
  unordered_map<string, int> last_printed;
public:
  bool shouldPrintMessage(int timestamp, string message) {
    if (last_printed.find(message) != last_printed.end()) {
      if (timestamp >= 10 + last_printed[message]) {
        last_printed[message] = timestamp;
        return true;
      }
      return false;
    }
    
    last_printed[message] = timestamp;
    return true;
  }
};

