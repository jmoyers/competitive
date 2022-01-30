#include <future>
#include <iostream>
#include <queue>
#include <string>
#include <unordered_set>

using namespace std;

class Solution {
public:
  string get_domain(string &url) { return url.substr(7, url.find('/', 7) - 7); }

  vector<string> crawl(string startUrl, HtmlParser htmlParser) {
    unordered_set<string> visited{startUrl};
    queue<future<vector<string>>> futures;

    auto domain = get_domain(startUrl);

    futures.push(std::thread(&HtmlParser::getUrls, &htmlParser, startUrl));

    while (!futures.empty()) {
      auto urls = futures.front().get();
      futures.pop();

      for (auto &r : urls) {
        if (get_domain(r) == domain and visited.find(r) == visited.end()) {
          visited.insert(r);
          futures.push(std::thread(&HtmlParser::getUrls, &htmlParser, r));
        }
      }
    }

    vector<string> results(visited.begin(), visited.end());
    return results;
  }
};