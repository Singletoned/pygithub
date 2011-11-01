# -*- coding: utf-8 -*-

import json

import requests
import werkzeug

make_url = werkzeug.Href("https://api.github.com/")

def _get_data(api_url):
    response = requests.get(api_url)
    content = response.content
    data = json.loads(content)
    return data


class Github(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        response = requests.get(
            make_url(),
            auth=(self.username, self.password))

    @property
    def user(self):
        url = make_url("users", self.username)
        data = _get_data(url)
        user = User(data)
        return user


class BaseModel(object):
    def __init__(self, data):
        self._data = data
        for key in self._keys:
            setattr(self, key, data[key])

class User(BaseModel):
    _keys = ['name', 'email', 'login']

    def __eq__(self, other):
        if self.login == other.login:
            return True
        return False

    @property
    def repos(self):
        url = make_url("users", self.login, "repos")
        data = _get_data(url)
        repos = [Repo(r) for r in data]
        return repos

    def get_repo(self, name):
        url = make_url("repos", self.login, name)
        data = _get_data(url)
        return Repo(data)


class Repo(BaseModel):
    _keys = ['name', 'git_url', 'html_url', 'owner']

    @property
    def user(self):
        url = make_url("users", self.owner['login'])
        data = _get_data(url)
        user = User(data)
        return user

    @property
    def issues(self):
        url = make_url("repos", self.user.login, self.name, "issues")
        data = _get_data(url)
        issues = [Issue(i) for i in data]
        return issues

    def get_issue(self, number):
        url = make_url("repos", self.user.login, self.name, "issues", number)
        data = _get_data(url)
        return Issue(data)

    @property
    def pulls(self):
        url = make_url("repos", self.user.login, self.name, "pulls")
        data = _get_data(url)
        return data


class Issue(BaseModel):
    _keys = ['title']

    @property
    def user(self):
        url = make_url("users", self._data['user']['login'])
        data = _get_data(url)
        user = User(data)
        return user
