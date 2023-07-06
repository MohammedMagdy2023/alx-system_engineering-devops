#!/usr/bin/env python3
import subprocess

# Set the remote and branch
remote = 'origin'
branch = 'master'

subprocess.run(['git', 'add','.'])
subprocess.run(['git', 'commit','-m', "shell permissions"])


# Run the git push command
subprocess.run(['git', 'push', remote, branch])

