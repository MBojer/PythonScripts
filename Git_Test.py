#!/usr/bin/python

import git

print "MARKER"

repo = git.Repo("")

diff_as_patch = repo.index.diff(repo.commit('HEAD~1'), create_patch=True)
print(diff_as_patch)

print "test marker"

print "end"
