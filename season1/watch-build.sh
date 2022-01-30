#!/bin/bash
inotifywait -e close_write -m . |
  while read -r directory events filename; do
    if [ "$filename" = "$1.cpp" ]; then
      clang++ -std=c++17 -g $1.cpp -o build/$1 && build/$1
    fi
  done
