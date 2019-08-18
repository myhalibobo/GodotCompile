import os
os.system("scons platform=osx -j8")
os.system("cp -r misc/dist/osx_tools.app ./Godot.app")
os.system("mkdir -p Godot.app/Contents/MacOS")
os.system("cp bin/godot.osx.tools.64 Godot.app/Contents/MacOS/Godot")
os.system("chmod +x Godot.app/Contents/MacOS/Godot")