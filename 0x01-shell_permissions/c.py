#!/usr/bin/env python3
import os

# Get the current working directory
cwd = os.getcwd()

# List all files and directories in the current working directory
for file in os.listdir(cwd):
    if file == "README.md":
        continue
    else:
        os.chmod(file,0o777)


