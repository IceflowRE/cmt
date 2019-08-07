#!/bin/sh
# executed from project root
mkdir dist
mkdir build
rm -rf ./build/cmt

# blender 2.8
cp -r ./cmt/ ./build/
cat ./blender/2_80.py >> ./build/cmt/__init__.py
cd ./build
zip -FSr ../dist/blender_cmt_2_80.zip ./cmt
cd ..
#rm -rf ./build/cmt
