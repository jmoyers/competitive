"""
---
title: Find Duplicate File in System
difficulty: medium
level: 2
links: 
- https://leetcode.com/problems/find-duplicate-file-in-system
---
Given a list of directory info including directory path, and all the files
with contents in this directory, you need to find out all the groups of
duplicate files in the file system in terms of their paths.

A group of duplicate files consists of at least two files that have exactly
the same content.

A single directory info string in the input list has the following format:

"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ...
fn.txt(fn_content)"

It means there are n files (f1.txt, f2.txt ... fn.txt with content
f1_content, f2_content ... fn_content, respectively) in directory
root/d1/d2/.../dm. Note that n >= 1 and m >= 0. If m = 0, it means the
directory is just the root directory.

The output is a list of group of duplicate file paths. For each group, it
contains all the file paths of the files that have the same content. A file
path is a string that has the following format:

"directory_path/file_name.txt"

Example 1:

Input:
["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d
4.txt(efgh)", "root 4.txt(efgh)"]

Output:  
[["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]

 

Note:

    No order is required for the final output.

    You may assume the directory name, file name and file content only has
    letters and digits, and the length of file content is in the range of
    [1,50].

    The number of files given is in the range of [1,20000].

    You may assume no files or directories share the same name in the same
    directory.

    You may assume each given directory info represents a unique directory.
    Directory path and file info are separated by a single blank space.

 
Follow-up beyond contest:

    Imagine you are given a real file system, how will you search files? DFS
    or BFS?

    If the file content is very large (GB level), how will you modify your
    solution?

    If you can only read the file by 1kb each time, how will you modify your
    solution?

    What is the time complexity of your modified solution? What is the most
    time-consuming part and memory consuming part of it? How to optimize?

    How to make sure the duplicated files you find are not false positive?
"""

from typing import List
from collections import defaultdict


class Solution:
    """
    What immediately comes to mind is hashing the file contents.

    Dictionary
    Hash(contents) -> full path name

    We since the contents are given as 1 < len < 50, we can probably
    just use the built in dictionary string hashing in python to do the
    hashing.

    https://www.asmeurer.com/blog/posts/what-happens-when-you-mess-with-hashing-in-python/
    
    'Note, the hashes you see below may not be the same ones you see if you
    run the examples, because Python hashing depends on the architecture of
    the machine you are running on, and, in newer versions of Python, hashes
    are randomized for security purposes.'

    This means that such a design is not suitable for distributed computing.
    You could use a cryptographic hashing funciton at that point like
    md5, sha, sha256 etc. At that point, the chance of accidental collision
    is extremely small (though file contents could be _designed_ to defeat
    the hashing algorithm). It depends on how security critical such a comparison
    is, but assuming its just for arbitrarily checking for file duplicates, 
    a hashing algorithm such as the ones above is fine in 2020.

    The below is a touch slow because we're using string concatentation and
    a state machine. With the protocol being this simple and straightfoward,
    we could be using indexes or simple built in split() in python for a 
    dramatic speedup (constant, this is still O(n) on total length of all
    strings.
    """

    def findDuplicates(self, paths: List[str]) -> List[List[str]]:
        by_contents = defaultdict(lambda: [])

        for p in paths:
            state = "r"
            # root - r
            # file - f
            # content - c

            root = ""
            file = ""
            content = ""

            for c in p:
                if c == " " and state == "f":
                    continue
                elif c == " " and state == "r":
                    file = root + "/"
                    state = "f"
                    continue
                elif c == "(":
                    state = "c"
                    continue
                elif c == ")":
                    by_contents[content].append(file)

                    content = ""
                    file = root + "/"
                    state = "f"
                    continue

                if state == "r":
                    root += c
                elif state == "f":
                    file += c
                elif state == "c":
                    content += c

        return [v for v in by_contents.values() if len(v) > 1]


def test_1():
    input = [
        "root/a 1.txt(abcd) 2.txt(efgh)",
        "root/c 3.txt(abcd)",
        "root/c/d 4.txt(efgh)",
        "root 4.txt(efgh)",
    ]
    out = set(
        [
            ("root/a/2.txt", "root/c/d/4.txt", "root/4.txt"),
            ("root/a/1.txt", "root/c/3.txt"),
        ]
    )

    results = Solution().findDuplicates(input)
    set_results = set()

    for r in results:
        set_results.add(tuple(r))

    assert set_results == out
