from concurrent.futures import ThreadPoolExecutor
from threading import Lock, Condition
from collections import deque
from typing import List

class Solution:
    def __init__(self):
        self.lock = Lock()
        self.cv = Condition(self.lock)
        self.q = deque()
        self.visited = set()
        self.pending = 0

        self.domain = None

    def get_domain(self, url):
        found = url.find("/", 7)

        if found == -1:
            return url[7:]
        else:
            return url[7:found]

    def work_available(self):
        return self.q or (not self.q and not self.pending)

    def retrieve(self, parser):
        while True:
            url = None

            with self.cv:
                self.cv.wait_for(self.work_available)

                if not self.q and not self.pending:
                    return

                self.pending += 1
                url = self.q.popleft()

            urls = parser.getUrls(url)

            with self.lock:
                self.pending -= 1
                for u in urls:
                    if u not in self.visited and self.get_domain(u) == self.domain:
                        self.visited.add(u)
                        self.q.append(u)
                self.cv.notify_all()

    def crawl(self, startUrl: str, htmlParser: "HtmlParser") -> List[str]:
        self.domain = self.get_domain(startUrl)
        self.visited.add(startUrl)
        self.q.append(startUrl)

        with ThreadPoolExecutor(max_workers=16) as pool:
            futures = [pool.submit(self.retrieve, htmlParser) for _ in range(16)]

            for f in futures:
                f.result()

            return [url for url in self.visited]

