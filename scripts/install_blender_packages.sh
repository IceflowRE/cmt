#!/bin/sh
# executed from project root
rm -rf "C:/Users/iceflower/AppData/Roaming/Blender Foundation/Blender/2.80/scripts/addons/cmt/"

# blender 2.8
cp -r ./cmt/ "C:/Users/iceflower/AppData/Roaming/Blender Foundation/Blender/2.80/scripts/addons/"
cat ./blender/2_80.py >> "C:/Users/iceflower/AppData/Roaming/Blender Foundation/Blender/2.80/scripts/addons/cmt/__init__.py"
