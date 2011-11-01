# -*- coding: utf-8 -*-

responses = {
    'https://api.github.com/': "",
    'https://api.github.com/users/Singletoned': '''{
        "login": "Singletoned",
        "html_url": "https://github.com/Singletoned",
        "email": "singletoned@gmail.com",
        "name": "Ed Singleton",
        "url": "https://api.github.com/users/Singletoned"}''',
    'https://api.github.com/users/Singletoned/repos': '''[{
        "language": "Python",
        "svn_url": "https://svn.github.com/Singletoned/pygithub",
        "html_url": "https://github.com/Singletoned/pygithub",
        "clone_url": "https://github.com/Singletoned/pygithub.git",
        "fork": false,
        "ssh_url": "git@github.com:Singletoned/pygithub.git",
        "description": "A vague attempt at a GitHub api3 library in Python",
        "private": false,
        "owner": {
          "login": "Singletoned",
          "url": "https://api.github.com/users/Singletoned"
        },
        "name": "pygithub",
        "url": "https://api.github.com/repos/Singletoned/pygithub",
        "git_url": "git://github.com/Singletoned/pygithub.git"}]''',
    'https://api.github.com/repos/Singletoned/pygithub': '''{
        "has_issues": true,
        "language": "Python",
        "svn_url": "https://svn.github.com/Singletoned/pygithub",
        "html_url": "https://github.com/Singletoned/pygithub",
        "clone_url": "https://github.com/Singletoned/pygithub.git",
        "fork": false,
        "ssh_url": "git@github.com:Singletoned/pygithub.git",
        "description": "A vague attempt at a GitHub api3 library in Python",
        "private": false,
        "owner": {
          "login": "Singletoned",
          "url": "https://api.github.com/users/Singletoned"
        },
        "name": "pygithub",
        "url": "https://api.github.com/repos/Singletoned/pygithub",
        "has_wiki": true,
        "git_url": "git://github.com/Singletoned/pygithub.git"}''',
    'https://api.github.com/repos/Singletoned/pygithub/issues': '''[{
        "body": "A test issue for testing the API",
        "state": "open",
        "labels": [{
            "color": "0b02e1",
            "name": "testing",
            "url": "https://api.github.com/repos/Singletoned/pygithub/labels/testing"}],
        "number": 2,
        "closed_at": null,
        "html_url": "https://github.com/Singletoned/pygithub/issues/2",
        "pull_request": {
          "patch_url": null,
          "html_url": null,
          "diff_url": null
        },
        "milestone": null,
        "assignee": null,
        "created_at": "2011-10-31T22:54:41Z",
        "user": {
          "login": "Singletoned",
          "url": "https://api.github.com/users/Singletoned",
          "id": 6284
        },
        "url": "https://api.github.com/repos/Singletoned/pygithub/issues/2",
        "comments": 0,
        "title": "Test Issue",
        "id": 2103140}]'''}

class MockRequest(object):
    def __init__(self, data):
        self.content = data

class MockRequests(object):
    @staticmethod
    def get(url, auth=None):
        return MockRequest(responses[url])
