# CPPBuildAid

## Current version is: 1.1.0

## Description:
This is a small script that helps with building C++ and C projects using cmake. I guess there are many such things, but this is mine. The script should be placed in the root directory of the project CMakeLists.txt. This script will create several lists of source files in a ```cmakeListings``` directory in the same directory of this script. The directories are listed as absolute and relative paths in relation to this script. Lists of all found headers and source files are also generated. One can use those lists in cmake like this:

```
file(STRINGS "includeDirsAbs.cmake" includes)
file(STRINGS "sourceFiles.cmake" sources)

include_directories(${includes})

add_executable(<TEST> ${sources})
```

This makes building easier because no one has to keep track of those files, they are added to the list files recursively.
This script will scan header and source files in specified directories, and all subdirectories.

This script also counts code lines from headers and source code files. It will also ignore files in specified directories from beeing counted.

To tell CPPBuildAid where to search one needs a ```projectDescription.xml``` right next to the script. This is an example for that file, it is pretty self explanatory:

```
<ProjectDescription>
    <IncludeDirs>
        <Dir path="include"/>
    </IncludeDirs>
    <SourceDirs>
        <Dir path="src"/>
    </SourceDirs>
    <NotCountedDirs>
        <Dir path="include/deps"/>
        <Dir path="include/dependencies"/>
        <Dir path="include/ext"/>
        <Dir path="include/external"/>
        <Dir path="src/deps"/>
        <Dir path="src/dependencies"/>
        <Dir path="src/ext"/>
        <Dir path="src/external"/>
    </NotCountedDirs>
</ProjectDescription>
```

## Options:
Currently CPPBuildAid supports these options:
* -b --buildType -> debug(default)/release
* -t --numberOfBuildThreads -> 1(default)/any unsigned integer except zero
* -i --installLocal -> if specified the install command of cmake will be executed. With this one can install a shared library on a system for example. This might require privilege levels
* -s --useSwig -> when specified swig will be used to generate a wrapper for a native shared library. CMake has to compile a shared library to use this
* -l --swigLanguage -> the language swig should wrap for. Only Python is supportrt with "python"
