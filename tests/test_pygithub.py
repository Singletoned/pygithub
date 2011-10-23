# -*- coding: utf-8 -*-

import os

import github

cfg = open(os.path.expanduser('~/.github')).read()
username, password = cfg.split(':', 1)

def test_user():
    gh = github.Github(username, password)
    user = gh.user
    assert user['name'] == "Ed Singleton"
    assert user['email'] == "singletoned@gmail.com"
