# CppBuildAid

This is a small script that helps with building C++ and C projects using cmake. I guess there are many such things, but this is mine. The script should be placed in the root directory of the project right next to the build directory.

Currently it supports these options:
* -bt --buildType -> debug(default)/release
* -nbt --numberOfBuildThreads -> 1(default)/any positive value except zero