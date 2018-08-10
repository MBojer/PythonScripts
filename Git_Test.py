#!/usr/bin/python

import git
repo = git.Repo("https://github.com/MBojer/PythonScripts.git")

print "MARKER"

repo.index.diff(repo.head.commit)
