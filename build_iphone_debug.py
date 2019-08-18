import os


os.system("scons p=iphone tools=no target=debug arch=arm -j8")
os.system("scons p=iphone tools=no target=debug arch=arm64 -j8")
# os.system("scons p=iphone tools=no target=debug arch=x86_64 -j8")

cpath = os.path.abspath('.')
os.chdir(os.path.join(cpath,"bin"))

os.system("lipo -create libgodot.iphone.debug.arm.a libgodot.iphone.debug.arm64.a -output libgodot.iphone.debug.fat.a")
# os.system("lipo -create libgodot.iphone.debug.arm.a libgodot.iphone.debug.arm64.a libgodot.iphone.debug.x86_64.a -output libgodot.iphone.debug.fat.a")
