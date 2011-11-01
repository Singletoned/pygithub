# -*- coding: utf-8 -*-

import os

import github

import mock_data

cfg = open(os.path.expanduser('~/.github')).read()
username, password = cfg.split(':', 1)

github.requests = mock_data.MockRequests
gh = github.Github(username, password)

def test_user():
    user = gh.user
    assert user.name == "Ed Singleton"
    assert user.email == "singletoned@gmail.com"
    assert isinstance(user, github.User)
    assert user._data['name'] == "Ed Singleton"

def test_repos():
    user = gh.user
    repos = user.repos
    repo_names = [r.name for r in repos]
    assert "pygithub" in repo_names

    repo = user.get_repo('pygithub')
    assert repo.user == user
    assert repo.name == u"pygithub"
    assert repo.html_url == u'https://github.com/Singletoned/pygithub'
    assert repo.git_url == u'git://github.com/Singletoned/pygithub.git'
    assert isinstance(repo, github.Repo)
    assert repo._data['language'] == "Python"

def test_issues():
    repo = gh.user.get_repo('pygithub')
    issue_titles = [i.title for i in repo.issues]
    assert "Test Issue" in issue_titles

    issue = repo.get_issue(2)
    assert isinstance(issue, github.Issue)
    assert issue.title == "Test Issue"
    assert issue._data['body'] == "A test issue for testing the API"
    assert issue.user == gh.user

def test_pulls():
    repo = gh.user.get_repo('pygithub')
    pull_titles = [p['title'] for p in repo.pulls]
    assert "Test Pull Request" in pull_titles
