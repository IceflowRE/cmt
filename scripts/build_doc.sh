#!/bin/sh
# executed from project root

rm -rf ./build/doc/

sphinx-build -b html ./doc/ ./build/doc/html/
#sphinx-build -b linkcheck ./doc/ ./build/doc/linkcheck/
