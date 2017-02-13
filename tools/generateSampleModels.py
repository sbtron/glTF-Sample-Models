#!/usr/bin/env python

import glob, os, subprocess

version = "2.0"

os.chdir("../collada")
for dir in os.listdir("."):
    os.chdir(dir)
    for file in glob.glob("*.dae"):
        name = file.replace(".dae", "")
        separatePath = "../../" + version + "/" + dir + "/glTF/"
        if not os.path.exists(separatePath):
            os.makedirs(separatePath)
        subprocess.call(["../../tools/COLLADA2GLTF.exe", "-i", file, "-o", separatePath + name + ".gltf", "-s"])

        embeddedPath = "../../" + version + "/" + dir + "/glTF-Embedded/"
        if not os.path.exists(embeddedPath):
            os.makedirs(embeddedPath)
        subprocess.call(["../../tools/COLLADA2GLTF.exe", "-i", file, "-o", embeddedPath + name + ".gltf"])

        materialCommonPath = "../../" + version + "/" + dir + "/glTF-MaterialsCommon/"
        if not os.path.exists(materialCommonPath):
            os.makedirs(materialCommonPath)
        subprocess.call(["../../tools/COLLADA2GLTF.exe", "-i", file, "-o", materialCommonPath + name + ".gltf", "-s", "-m"])

        binaryPath = "../../" + version + "/" + dir + "/glTF-Binary/"
        if not os.path.exists(binaryPath):
            os.makedirs(binaryPath)
        subprocess.call(["../../tools/COLLADA2GLTF.exe", "-i", file, "-o", binaryPath + name + ".glb", "-b"])
        break
    os.chdir("..")
