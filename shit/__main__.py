# -*- coding=utf-8 -*-
from __future__ import absolute_import, division, unicode_literals

import os
import sys

if __name__ == "__main__":
    shitignore = {}
    if os.path.exists(".shitignore"):
        for line in open(".shitignore").readlines():
            line = line.strip()
            if not line:
                continue

            if b" | " in line:
                needle, replacement = line.rsplit(b" | ", 1)
            else:
                needle, replacement = line, b"<...>"
            shitignore[needle] = replacement
    else:
        print "No .shitignore found in current directory"
        sys.exit(1)

    if not os.path.exists(".shit"):
        os.mkdir(".shit")

    cwd = os.getcwd()
    shit = os.path.join(cwd, ".shit")

    for root, dirs, files in os.walk(shit):
        if root.startswith(os.path.join(shit, ".git")):
            continue

        for file in files:
            if not os.path.exists(os.path.join(cwd, os.path.relpath(root, shit), file)):
                os.unlink(os.path.join(shit, root, file))

    shitignore_unused = set(shitignore.keys())
    for root, dirs, files in os.walk(cwd):
        for i, dir in enumerate(dirs):
            if root == cwd and dir.startswith(".shit"):
                del dirs[i]
                continue

            target_dir = os.path.join(shit, os.path.relpath(root, cwd), dir)
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

        for file in files:
            if root == cwd and file.startswith(".shit"):
                continue

            contents = open(os.path.join(root, file)).read()
            for k, v in shitignore.iteritems():
                if k in contents:
                    contents = contents.replace(k, v)
                    shitignore_unused.discard(k)

            target_file = os.path.join(shit, os.path.relpath(root, cwd), file)
            open(target_file, "w").write(contents)

    if shitignore_unused:
        print("Warning: the following .shitignore lines were not used:")
        for line in shitignore_unused:
            print(" * " + line)

    os.chdir(".shit")
    os.execvp("git", ["git"] + sys.argv[1:])
