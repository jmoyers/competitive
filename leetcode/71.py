"""
---
number: 71
title: Simplify Path
difficulty: Medium
tags:
- stack
- parsing
- string
---
Given an absolute path for a file (Unix-style), simplify it. Or in other
words, convert it to the canonical path.

In a UNIX-style file system, a period . refers to the current directory.
Furthermore, a double period .. moves the directory up a level.

Note that the returned canonical path must always begin with a slash /, and
there must be only a single slash / between two directory names. The last
directory name (if it exists) must not end with a trailing /. Also, the
canonical path must be the shortest string representing the absolute path.

 

Example 1:

Input: "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
Example 2:

Input: "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
Example 3:

Input: "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
Example 4:

Input: "/a/./b/../../c/"
Output: "/c"
Example 5:

Input: "/a/../../b/../c//.//"
Output: "/c"
Example 6:

Input: "/a//b////c/d//././/.."
Output: "/a/b/c"
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        hit slash, start director
        hit slash, end directory
        
        parse directory
            if empty, drop
            if ., drop
            if .., remove top of stack
            else push stack
            
        remove trailing slash
        ensure at least 1 character, is slash
        """

        stack = []
        start = None

        if path[-1] == "/":
            path = path[:-1]

        if path == "":
            return "/"

        for i, c in enumerate(path):
            if c == "/" and start is not None:
                directory = path[start + 1 : i]

                if directory == ".":
                    pass
                elif directory == "":
                    pass
                elif directory == "..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(directory)

            if c == "/":
                start = i

        if start != len(path) - 1:
            directory = path[start + 1 :]

            if directory == ".":
                pass
            elif directory == "":
                pass
            elif directory == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(directory)

        return "/" + "/".join(stack)
