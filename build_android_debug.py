import os

os.system("scons platform=android target=debug android_arch=armv7")
os.system("scons platform=android target=debug android_arch=arm64v8")

chdir("platform/android/java")

os.system("./gradlew clean")
os.system("./gradlew build")