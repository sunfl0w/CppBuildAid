# CPPBuildAid

## Description:
This is a small script that helps with building C++ and C projects using cmake. I guess there are many such things, but this is mine. The script should be placed in the root directory of the project right next to the ```src``` and ```include``` directories and the CMakeLists.txt. This script will create a includelist.cmake and a sourcelist.cmake with all source and header files to use in a CMakeLists.txt via:

```
file(STRINGS "includelist.cmake" includes)
file(STRINGS "sourcelist.cmake" sources)

include_directories(${includes})

add_executable(<TEST> ${sources})
```

This makes building easier beacause no one has to keep track of those files, they are added to the list files recursively.
This script will also scan and use ```source``` and ```include``` folders in a ```deps``` directory in the projects root directory. This is for the code of dependencies.

This script also counts code lines from headers and source code files in the ```src``` and ```include``` folders and prints the data.

## Options:
Currently it supports these options:
* -b --buildType -> debug(default)/release
* -t --numberOfBuildThreads -> 1(default)/any unsigned integer except zero
