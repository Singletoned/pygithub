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
        "id": 2103140}]''',
    "https://api.github.com/repos/Singletoned/pygithub/issues/2": '''{
        "body": "A test issue for testing the API",
        "state": "open",
        "labels": [
          {
            "color": "0b02e1",
            "name": "testing",
            "url": "https://api.github.com/repos/Singletoned/pygithub/labels/testing"
          }
        ],
        "number": 2,
        "closed_at": null,
        "pull_request": {
          "patch_url": null,
          "html_url": null,
          "diff_url": null
        },
        "milestone": null,
        "assignee": null,
        "closed_by": null,
        "created_at": "2011-10-31T22:54:41Z",
        "user": {
          "login": "Singletoned",
          "url": "https://api.github.com/users/Singletoned",
          "id": 6284
        },
        "html_url": "https://github.com/Singletoned/pygithub/issues/2",
        "url": "https://api.github.com/repos/Singletoned/pygithub/issues/2",
        "comments": 0,
        "title": "Test Issue",
        "id": 2103140}''',
    "https://api.github.com/repos/Singletoned/pygithub/pulls": '''[{
        "created_at": "2011-11-01T13:21:55Z",
        "title": "Test Pull Request",
        "patch_url": "https://github.com/Singletoned/pygithub/pull/3.patch",
        "html_url": "https://github.com/Singletoned/pygithub/pull/3",
        "_links": {
          "comments": {
            "href": "https://api.github.com/repos/Singletoned/pygithub/issues/3/comments"
          },
          "review_comments": {
            "href": "https://api.github.com/repos/Singletoned/pygithub/pulls/3/comments"
          },
          "html": {
            "href": "https://github.com/Singletoned/pygithub/pull/3"
          },
          "self": {
            "href": "https://api.github.com/repos/Singletoned/pygithub/pulls/3"
          }
        },
        "number": 3,
        "state": "open",
        "merged_at": null,
        "user": {
          "login": "Singletoned",
          "id": 6284,
          "url": "https://api.github.com/users/Singletoned"
        },
        "updated_at": "2011-11-01T13:30:55Z",
        "closed_at": null,
        "issue_url": "https://github.com/Singletoned/pygithub/issues/3",
        "id": 452102,
        "body": "This is a test Pull Request",
        "diff_url": "https://github.com/Singletoned/pygithub/pull/3.diff",
        "url": "https://api.github.com/repos/Singletoned/pygithub/pulls/3"}]''',
    "https://api.github.com/repos/Singletoned/pygithub/pulls/3": '''{
        "created_at": "2011-11-01T13:21:55Z",
        "merged": false,
        "comments": 0,
        "review_comments": 0,
        "closed_at": null,
        "title": "Test Pull Request",
        "head": {
          "sha": "4c121c83cf2ed51de71ef9f8606e2085e971bf86",
          "user": {
            "login": "Singletoned",
            "id": 6284,
            "url": "https://api.github.com/users/Singletoned"
          },
          "ref": "test",
          "repo": {
            "open_issues": 2,
            "created_at": "2011-10-29T20:55:11Z",
            "homepage": "",
            "language": "Python",
            "html_url": "https://github.com/Singletoned/pygithub",
            "fork": false,
            "private": false,
            "ssh_url": "git@github.com:Singletoned/pygithub.git",
            "svn_url": "https://svn.github.com/Singletoned/pygithub",
            "master_branch": null,
            "owner": {
              "login": "Singletoned",
              "id": 6284,
              "url": "https://api.github.com/users/Singletoned"
            },
            "name": "pygithub",
            "git_url": "git://github.com/Singletoned/pygithub.git",
            "clone_url": "https://github.com/Singletoned/pygithub.git",
            "description": "A vague attempt at a GitHub api3 library in Python",
            "id": 2672504,
            "url": "https://api.github.com/repos/Singletoned/pygithub"
          },
          "label": "Singletoned:test"
        },
        "patch_url": "https://github.com/Singletoned/pygithub/pull/3.patch",
        "number": 3,
        "mergeable": true,
        "_links": {
          "review_comments": {
            "href": "https://api.github.com/repos/Singletoned/pygithub/pulls/3/comments"
          },
          "comments": {
            "href": "https://api.github.com/repos/Singletoned/pygithub/issues/3/comments"
          },
          "html": {
            "href": "https://github.com/Singletoned/pygithub/pull/3"
          },
          "self": {
            "href": "https://api.github.com/repos/Singletoned/pygithub/pulls/3"
          }
        },
        "state": "open",
        "html_url": "https://github.com/Singletoned/pygithub/pull/3",
        "additions": 1,
        "user": {
          "login": "Singletoned",
          "id": 6284,
          "url": "https://api.github.com/users/Singletoned"
        },
        "diff_url": "https://github.com/Singletoned/pygithub/pull/3.diff",
        "merged_by": null,
        "changed_files": 1,
        "base": {
          "sha": "2e46249376de6c718e98e836f9903b803f44e2b0",
          "user": {
            "login": "Singletoned",
            "id": 6284,
            "url": "https://api.github.com/users/Singletoned"
          },
          "ref": "master",
          "repo": {
            "open_issues": 2,
            "created_at": "2011-10-29T20:55:11Z",
            "homepage": "",
            "language": "Python",
            "watchers": 2,
            "html_url": "https://github.com/Singletoned/pygithub",
            "fork": false,
            "private": false,
            "ssh_url": "git@github.com:Singletoned/pygithub.git",
            "svn_url": "https://svn.github.com/Singletoned/pygithub",
            "master_branch": null,
            "owner": {
              "login": "Singletoned",
              "id": 6284,
              "url": "https://api.github.com/users/Singletoned"
            },
            "name": "pygithub",
            "git_url": "git://github.com/Singletoned/pygithub.git",
            "clone_url": "https://github.com/Singletoned/pygithub.git",
            "description": "A vague attempt at a GitHub api3 library in Python",
            "id": 2672504,
            "url": "https://api.github.com/repos/Singletoned/pygithub"
          },
          "label": "Singletoned:master"
        },
        "updated_at": "2011-11-01T13:30:55Z",
        "issue_url": "https://github.com/Singletoned/pygithub/issues/3",
        "id": 452102,
        "commits": 2,
        "deletions": 0,
        "merged_at": null,
        "body": "This is a test Pull Request",
        "url": "https://api.github.com/repos/Singletoned/pygithub/pulls/3"}'''}

class MockRequest(object):
    def __init__(self, data):
        self.content = data

class MockRequests(object):
    @staticmethod
    def get(url, auth=None):
        return MockRequest(responses[url])
