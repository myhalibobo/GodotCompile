import os

os.system("scons platform=android target=release android_arch=armv7")
os.system("scons platform=android target=release android_arch=arm64v8")

chdir("platform/android/java")

os.system("./gradlew clean")
os.system("./gradlew build")