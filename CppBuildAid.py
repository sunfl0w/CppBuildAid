import sys
import argparse
import subprocess
import shutil
import os

print("Starting CppBuildAid")

argumentParser = argparse.ArgumentParser()
argumentParser.add_argument("-bt", "--buildType")
argumentParser.add_argument("-bl", "--buildLanguage")
argumentParser.add_argument("-nbt", "--numberOfBuildThreads")

args = argumentParser.parse_args()

typeOfBuild = "debug"
if(args.buildType is "release"):
    typeOfBuild = "release"

numberOfBuildThreads = 1
if(args.numberOfBuildThreads is not None):
    numberOfBuildThreads = args.numberOfBuildThreads
print("Using {} threads to build".format(numberOfBuildThreads))

if(os.path.exists("build")):
    shutil.rmtree("build")

print("Running cmake")

subprocess.call(["cmake", "-H.", "-Bbuild"])
subprocess.call(["cmake", "-DCMAKE_BUILD_TYPE={}".format(typeOfBuild.capitalize()), "."], cwd="build")
subprocess.call(["cmake", "--build", ".", "--", "-j", str(numberOfBuildThreads)], cwd="build")

print("Build completed successfully")