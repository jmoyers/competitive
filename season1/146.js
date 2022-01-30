// Design and implement a data structure for Least Recently Used (LRU) cache.
// It should support the following operations: get and put.
//
// get(key) - Get the value (will always be positive) of the key if the key
// exists in the cache, otherwise return -1.  put(key, value) - Set or insert
// the value if the key is not already present. When the cache reached its
// capacity, it should invalidate the least recently used item before inserting
// a new item.
//
// The cache is initialized with a positive capacity.
//
// Follow up: Could you do both operations in O(1) time complexity?
//
// Example:
//
// LRUCache cache = new LRUCache( 2 /* capacity */ );
//
// cache.put(1, 1);
// cache.put(2, 2);
// cache.get(1);       // returns 1
// cache.put(3, 3);    // evicts key 2
// cache.get(2);       // returns -1 (not found)
// cache.put(4, 4);    // evicts key 1
// cache.get(1);       // returns -1 (not found)
// cache.get(3);       // returns 3
// cache.get(4);       // returns 4

class Node {
  constructor(key, val, prev, next) {
    this.key = key;
    this.val = val;
    this.next = next;
    this.prev = prev;
  }
}

class LRUCache {
  constructor(size = 2) {
    // doubly linked list reflect the "order" of the hash table
    // where the tail reflects the least recently used item for
    // easy removal O(1)
    this.head = null;
    this.tail = null;
    // we'll keep a second reference to items stored in a hash map
    // to preserve O(1) lookup
    this.hash_table = {};
    this.hash_table_size = 0;
    this.size = size;
  }
  get(key) {
    // return the val for this key and update structure to
    // reflect this item was recently accessed
    // we'll remove the item from the linked list and insert it at the head
    if (!this.hash_table[key]) return -1;

    const item = this.hash_table[key];

    if (item === this.head) return item.val;

    this.put(item.key, item.val);

    return item.val;
  }
  remove(key) {
    if (!this.hash_table[key]) return;

    const item = this.hash_table[key];

    if (item.prev) item.prev.next = item.next;
    if (item.next) item.next.prev = item.prev;

    if (this.head === item) this.head = this.head.next;
    if (this.tail === item) this.tail = this.tail.prev;

    delete this.hash_table[key];
    this.hash_table_size--;
  }
  put(key, val) {
    this.remove(key);

    const item = new Node(key, val);

    if (this.head) {
      item.next = this.head;
      this.head.prev = item;
    }

    this.head = item;

    if (!this.tail) this.tail = this.head;

    this.hash_table[key] = item;
    this.hash_table_size++;

    // if over size remove least recently used item
    // to remove the item, we'll take the tail and move it to the previous
    // node and delete the entry from the hash_table storage
    if (this.hash_table_size > this.size) {
      this.remove(this.tail.key);
    }
  }
  debug() {
    if (!this.head) {
      return;
    }

    let visited = [];

    let result = "list: ";
    result += this.head.key;

    if (Object.keys(this.hash_table).length > 1) result += " -> ";

    let curr = this.head.next;

    while (curr) {
      if (visited.includes(curr.key)) {
        console.log(result, "cycle", curr.key);
        return;
      }
      visited.push(curr.key);
      result += curr.key;
      if (curr != this.tail) result += " -> ";
      curr = curr.next;
    }

    console.log(result);
  }
}

const lru = new LRUCache(2);
lru.put(2, 1);
lru.debug();
lru.put(3, 2);
lru.debug();
lru.get(3);
lru.debug();
lru.get(2);
lru.debug();
lru.put(4, 3);
lru.debug();
lru.get(2);
lru.debug();
lru.get(3);
lru.debug();
lru.get(4);
lru.debug();
