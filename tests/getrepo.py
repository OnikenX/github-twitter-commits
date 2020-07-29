#!/bin/python
from github import Github
reponame = input()
repo = Github().get_repo(reponame)
print(repo.name)
