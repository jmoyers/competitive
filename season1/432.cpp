#include <iostream>
#include <list>
#include <string>
#include <unordered_map>
#include <utility>
#include <assert.h>

using namespace std;

class AllOne {
 private:
  using Bucket = list<string>;
  using BucketList = list<Bucket>;
  using Record = tuple<int, BucketList::iterator, Bucket::iterator>;
  using Map = unordered_map<string, Record>;

  Map map;
  BucketList bucket_list;

  int valueForBucket(BucketList::iterator b) {
    string key = (*b).back();
    return get<0>(map[key]);
  }

  BucketList::iterator getBucket(int value, BucketList::iterator old_bucket) {
    int old_value = valueForBucket(old_bucket);

    if (old_value > value) {
      // the new value is smaller and therefore should be stored before
      // the current value
      if (old_bucket == bucket_list.begin()) {
        // this is the first bucket, so we need to create one for the
        // smaller value to live in
        bucket_list.push_front(Bucket{});
        return bucket_list.begin();
      } else {
        // there is a bucket before us, but we need to check
        // if its the right value
        if (valueForBucket(prev(old_bucket)) != value) {
          // because its not the right value, we need to add a bucket
          // between these two for the new value to live in
          bucket_list.insert(old_bucket, Bucket{});
        }

        return prev(old_bucket);
      }
    } else {
      // our new value is larger and therefore should be stored after
      // the current value
      if (next(old_bucket) == bucket_list.end()) {
        // our current bucket is the last one we have, so we need to create
        // a new one to store the value in
        bucket_list.push_back(Bucket{});
        return prev(bucket_list.end());
      } else {
        // there is a bucket after us, but we need to check if its
        // the right value
        if (valueForBucket(next(old_bucket)) != value) {
          bucket_list.insert(next(old_bucket), Bucket{});
        }

        return next(old_bucket);
      }
    }
  }
 public:
  void inc(string key) {
    if (map.find(key) != map.end()) {
      auto [old_value, old_bucket, old_it] = map[key];

      BucketList::iterator new_bucket = getBucket(old_value + 1, old_bucket);

      // add the key to its new bucket
      (*new_bucket).push_back(key);

      // replace its map entry with the new bucket
      map[key] = Record(old_value + 1, new_bucket, prev((*new_bucket).end()));

      // erase the old entry old_bucket old_bucket
      (*old_bucket).erase(old_it);
      
      // if that old_bucket is empty, get rid of it to maintain O(1)
      // min and max
      if ((*old_bucket).empty()) {
        bucket_list.erase(old_bucket);
      }
    } else {
      // if we have a new key that will start at 1
      // ensure we have at least one bucket and its value is 1
      if (bucket_list.empty() or 
          valueForBucket(bucket_list.begin()) != 1) {
        bucket_list.push_front(Bucket{});
      } 

      // okay, our target bucket should be the first one!
      BucketList::iterator bucket = bucket_list.begin();
      (*bucket).push_back(key);
      map[key] = Record(1, bucket, prev((*bucket).end()));
    }
  }

  void dec(string key) {
    if (map.find(key) == map.end()) {
      return;
    }

    auto [old_value, old_bucket, old_it] = map[key];

    // remove the value completely if it was 1, including
    // the bucket if it was empty so we can always get the minimum
    if (old_value - 1 == 0) {
      (*old_bucket).erase(old_it);

      if ((*old_bucket).empty()) {
        bucket_list.erase(old_bucket);
      }
      map.erase(key);
      return;
    }

    BucketList::iterator new_bucket = getBucket(old_value - 1, old_bucket);

    // add the key to its new bucket
    (*new_bucket).push_back(key);

    // replace its map entry with the new bucket
    map[key] = Record(old_value - 1, new_bucket, prev((*new_bucket).end()));

    // erase the old entry old_bucket old_bucket
    (*old_bucket).erase(old_it);

    // if that old_bucket is empty, get rid of it to maintain O(1)
    // min and max
    if ((*old_bucket).empty()) {
      bucket_list.erase(old_bucket);
    }
  }

  string getMaxKey() {
    if (bucket_list.empty()) return "";
    return bucket_list.back().front();
  }

  string getMinKey() {
    if (bucket_list.empty()) return "";
    return bucket_list.front().front();
  }
};

void test1 () {
  AllOne ao;
  ao.inc("a");
  ao.inc("a");
  ao.inc("a");
  ao.inc("a");
  ao.inc("a");
  ao.inc("a");
  ao.inc("a");
  ao.inc("b");
  assert(ao.getMinKey() == "b");
  ao.inc("b");
  assert(ao.getMinKey() == "b");
  ao.inc("c");
  ao.dec("c");
  assert(ao.getMinKey() == "b");
}

void test2 () {
  AllOne ao;
  ao.inc("a"); // 1
  ao.inc("b"); // 1
  ao.inc("b"); // 2
  ao.inc("c"); // 1
  ao.inc("c"); // 2 
  ao.inc("c"); // 3
  ao.dec("b"); // 1
  ao.dec("b"); // delete
  assert(ao.getMinKey() == "a");
  ao.dec("a"); // delete
  assert(ao.getMaxKey() == "c");
  assert(ao.getMinKey() == "c");
}

void test3() {
  AllOne ao;
  ao.inc("hello"); // 1
  ao.inc("world"); // 1
  ao.inc("leet");// 1
  ao.inc("code");// 1
  ao.inc("DS");// 1
  ao.inc("leet");// 2
  assert(ao.getMaxKey() == "leet");
  ao.inc("DS");// 2
  ao.dec("leet"); //1
  assert(ao.getMaxKey() == "DS");
  ao.dec("DS");// 1
  ao.inc("hello");// 2
  assert(ao.getMaxKey() == "hello");
  ao.inc("hello");// 3
  ao.inc("hello");// 4 <- min
  ao.dec("world");// delete
  ao.dec("leet");// delete
  ao.dec("code");// delete
  ao.dec("DS");// delete
  assert(ao.getMaxKey() == "hello");
  ao.inc("new");// 1
  ao.inc("new");// 2
  ao.inc("new");// 3
  ao.inc("new");// 4
  ao.inc("new");// 5
  ao.inc("new");// 6
  assert(ao.getMaxKey() == "new");
  assert(ao.getMinKey() == "hello");
}

void test4() {
  AllOne ao;
  ao.inc("hello"); // 1
  ao.inc("goodbye"); // 1
  ao.inc("hello"); // 2
  ao.inc("hello"); // 3
  assert(ao.getMaxKey() == "hello");

  ao.inc("leet"); // 1
  ao.inc("code"); // 1
  ao.inc("leet"); // 2
  ao.dec("hello"); // 2
  ao.inc("leet"); // 3
  ao.inc("code"); // 2
  ao.inc("code"); // 3
  cout << ao.getMaxKey() << endl;
  assert(ao.getMaxKey() == "leet");
}

int main() {
  test1();
  test2();
  test3();
  test4();
}
