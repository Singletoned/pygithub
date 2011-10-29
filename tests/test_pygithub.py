# -*- coding: utf-8 -*-

import os

import github

cfg = open(os.path.expanduser('~/.github')).read()
username, password = cfg.split(':', 1)
gh = github.Github(username, password)

def test_user():
    user = gh.user
    assert user.name == "Ed Singleton"
    assert user.email == "singletoned@gmail.com"
    assert isinstance(user, github.User)

def test_repos():
    user = gh.user
    repos = user.repos
    repo_names = [r.name for r in repos]
    assert "testino" in repo_names
