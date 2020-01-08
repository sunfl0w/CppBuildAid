import sys
import argparse
import subprocess
import shutil
import os
from datetime import datetime

print("Starting CppBuildAid")
startTime = datetime.now()

argumentParser = argparse.ArgumentParser()
argumentParser.add_argument("-bt", "--buildType", default="debug")
argumentParser.add_argument("-pt", "--publishingType", default="executable")
argumentParser.add_argument("-bl", "--buildLanguage", default="C++")
argumentParser.add_argument("-nbt", "--numberOfBuildThreads", default=1)

args = argumentParser.parse_args()

numberOfBuildThreads = 1
if(args.numberOfBuildThreads is not None and args.numberOfBuildThreads >= 1):
    numberOfBuildThreads = args.numberOfBuildThreads
print("Using {} threads to build".format(numberOfBuildThreads))

if(os.path.exists("build")):
    shutil.rmtree("build")

print("Running cmake")

subprocess.call(["cmake", "-H.", "-Bbuild"])
subprocess.call(
    ["cmake", "-DCMAKE_BUILD_TYPE={}".format(args.buildType.capitalize()), "."], cwd="build")
subprocess.call(["cmake", "--build", ".", "--", "-j",
                 str(numberOfBuildThreads)], cwd="build")

print("Build completed successfully in {} ms.".format(datetime.now() - startTime))
