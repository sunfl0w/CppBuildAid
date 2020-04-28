import sys
import argparse
import subprocess
import shutil
import os


def main(argv):
    build()


if __name__ == "__main__":
    main(sys.argv)


def build(argv):
    print("Starting CppBuildAid")

    argumentParser = argparse.ArgumentParser()
    argumentParser.add_argument("-bt", "--buildType")
    argumentParser.add_argument("-bl", "--buildLanguage")
    argumentParser.add_argument("-t", "--threads")

    args = argumentParser.parse_args()

    typeOfBuild = "debug"
    if(args.buildType == "release"):
        typeOfBuild = "release"

    threads = 1
    if(args.threads is not None and args.threads >= 1):
        threads = args.threads

    print("Running cmake")
    print("Using {} threads to build in {}-mode".format(threads, typeOfBuild))

    resultBuildType = subprocess.call(["cmake", "-DCMAKE_BUILD_TYPE={}".format(typeOfBuild.capitalize()), "."], cwd="build")
    resultBuild = subprocess.call(["cmake", "--build", ".", "-j", str(threads)], cwd="build")

    print("Build process completed")
    if(resultBuildType == 0 or resultBuild == 0):
        print("Build failes with errors")


def generateSourceList():
    pass


def generateIncludeList():
    pass