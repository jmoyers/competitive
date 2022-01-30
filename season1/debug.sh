#!/bin/bash
clang++ -std=c++17 -g $1 -o build/$1 && lldb build/$1
