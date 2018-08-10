#!/usr/bin/python

import git
repo = git.Repo("https://github.com/MBojer/PythonScripts.git")

print "MARKER"

repo = git.Repo('repo_path')
commits_list = list(repo.iter_commits())

# --- To compare the current HEAD against the bare init commit
a_commit = commits_list[0]
b_commit = commits_list[-1]

a_commit.diff(b_commit)
