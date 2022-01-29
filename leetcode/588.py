"""
---
title: Design In-Memory File System
difficulty: hard
tags:
- design
- hash map
- parsing
companies:
- amazon
links:
- https://leetcode.com/problems/design-in-memory-file-system/
---

Design an in-memory file system to simulate the following functions:

ls: Given a path in string format. If it is a file path, return a list that only
contains this file's name. If it is a directory path, return the list of file
and directory names in this directory. Your output (file and directory names
together) should in lexicographic order.

mkdir: Given a directory path that does not exist, you should make a new
directory according to the path. If the middle directories in the path don't
exist either, you should create them as well. This function has void return
type.

addContentToFile: Given a file path and file content in string format. If the
file doesn't exist, you need to create that file containing given content. If
the file already exists, you need to append given content to original content.
This function has void return type.

readContentFromFile: Given a file path, return its content in string format.


Example:

Input: ["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
[[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]

Output: [null,[],null,null,["a"],"hello"]

Explanation: https://assets.leetcode.com/uploads/2018/10/12/filesystem.png


Note:

    You can assume all file or directory paths are absolute paths which begin
    with / and do not end with / except that the path is just "/".

    You can assume that all operations will be passed valid parameters and
    users will not attempt to retrieve file content or list a directory or
    file that does not exist.

    You can assume that all directory names and file names only contain
    lower-case letters, and same names won't exist in the same directory.
"""
from typing import List
import typing


class FileSystem:
    """
    Options for data structure.

    1. strictly dictionary
        - use introspection to determine record type
        - file value is a string
        - directory value is a dictionary
        - benefits
            - O(path parts) lookup, split on "/"
            - O(path parts) write
        - downside
            - typing not explicit
            - file systems usually have stats like:
                - mtime, atime, mounting devices etc
    2. dictionary with a node class
        - have a class that represents a file system node
        - still do store it in a dictionary, but each key
            points to a node, which has a type, children or contents
            and can be expanded for other stat like properties
        - node can have contents or children
        - has a type (DIR, FILE for now)
        - benefits
            - type explicit
        - downside
            - more class furniture
    
    Given the requirements, I think we go with option 1 for now and we
    could discuss option 2 if there are followups for how to deal with
    expanded requirements.

    Type 1 structure:

    store = {
        "/": {
            "dir1": {
                "file1": "",
                "file2": ""
            },
            "dir2": {
                "file1": "File contents"
            }
        }
    }
    """

    def __init__(self):
        self.store = {"/": {}}

    def ls(self, path: str) -> List[str]:
        path = path.split("/")

        path[0] = "/"

        target = self.store

        for p in path[: len(path) - 1]:
            if p == "":
                target = target["/"]
            elif p in target and type(target) == dict:
                target = target[p]

        fileOrDir = path[-1]

        if fileOrDir == "":
            return sorted(list(target.keys()))
        elif type(target[fileOrDir]) == str:
            return [fileOrDir]
        else:
            return sorted(list(target[fileOrDir].keys()))

    def mkdir(self, path: str) -> None:
        parts = path.split("/")

        parts[0] = "/"

        target = self.store

        for p in parts:
            if p in target:
                target = target[p]
            else:
                target[p] = {}
                target = target[p]

    def addContentToFile(self, filePath: str, content: str) -> None:
        path = filePath.split("/")

        target = self.store

        for p in path[: len(path) - 1]:
            if p == "":
                target = target["/"]
            elif p in target and type(target) == dict:
                target = target[p]

        file = path[-1]

        if file in target:
            target[file] = target[file] + content
        else:
            target[file] = content

    def readContentFromFile(self, filePath: str) -> str:
        path = filePath.split("/")

        target = self.store

        for p in path:
            if p == "":
                target = target["/"]
            elif p in target:
                target = target[p]

        return target


def test_lc1():
    fs = FileSystem()

    assert fs.ls("/") == []

    fs.mkdir("/a/b/c")

    assert fs.ls("/a/b") == ["c"]

    fs.mkdir("/a/b/a")

    assert fs.ls("/a/b") == ["a", "c"]


def test_write_and_read():
    fs = FileSystem()

    content = "testing hello"

    fs.addContentToFile("/test", content)

    assert fs.readContentFromFile("/test") == content


def test_mkdir_and_write():
    fs = FileSystem()
    fs.mkdir("/test/test1/test2")
    fs.addContentToFile("/test/test1/test2/file1", "test")
    fs.addContentToFile("/test/test1/test2/file1", "test")
    assert fs.readContentFromFile("/test/test1/test2/file1") == "testtest"


def test_append():
    fs = FileSystem()

    content = "testing hello"

    fs.addContentToFile("/test", content)
    fs.addContentToFile("/test", content)

    assert fs.readContentFromFile("/test") == content + content


def test_mkdir():
    fs = FileSystem()

    fs.mkdir("/test/test2/test3")

    assert fs.store == {"/": {"test": {"test2": {"test3": {}}}}}


def test_ls():
    fs = FileSystem()

    assert fs.ls("/") == []

    fs.mkdir("/test")

    assert fs.ls("/") == ["test"]
    assert fs.ls("/test") == []

    fs.mkdir("/test/test1")

    assert fs.ls("/") == ["test"]

    assert fs.ls("/test") == ["test1"]

    fs.addContentToFile("/test/test1/file1", "test")

    assert fs.ls("/test/test1") == ["file1"]
    fs.addContentToFile("/test/test1/file2", "test")
    assert fs.ls("/test/test1") == ["file1", "file2"]
