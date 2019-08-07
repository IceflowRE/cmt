#!/bin/sh
# executed from project root

rm -rf ./build/doc/

sphinx-build -b html ./doc/source/ ./build/doc/html/
#sphinx-build -b linkcheck ./doc/source/ ./build/doc/linkcheck/
