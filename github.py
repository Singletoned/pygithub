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


class UserOwnedModel(BaseModel):
    @property
    def user(self):
        url = make_url("users", self.owner['login'])
        data = _get_data(url)
        user = User(data)
        return user


class UserLinkedModel(BaseModel):
    @property
    def user(self):
        url = make_url("users", self._data['user']['login'])
        data = _get_data(url)
        user = User(data)
        return user


class User(BaseModel):
    _keys = ['name', 'email', 'login']

    def __eq__(self, other):
        if self.login == other.login:
            return True
        return False

    @property
    def repos(self):
        return Repo.get_all(self)

    def get_repo(self, name):
        return Repo.get(self, name)


class Repo(UserOwnedModel):
    _keys = ['name', 'git_url', 'html_url', 'owner']

    @classmethod
    def get_all(cls, user):
        url = make_url("users", user.login, "repos")
        data = _get_data(url)
        repos = [cls(r) for r in data]
        return repos

    @classmethod
    def get(cls, user, name):
        url = make_url("repos", user.login, name)
        data = _get_data(url)
        return cls(data)

    @property
    def issues(self):
        return Issue.get_all(self)

    def get_issue(self, number):
        return Issue.get(self, number)

    @property
    def pulls(self):
        return Pull.get_all(self)

    def get_pull(self, number):
        return Pull.get(self, number)


class Issue(UserLinkedModel):
    _keys = ['title']

    @classmethod
    def get_all(cls, repo):
        url = make_url("repos", repo.user.login, repo.name, "issues")
        data = _get_data(url)
        issues = [cls(i) for i in data]
        return issues

    @classmethod
    def get(cls, repo, number):
        url = make_url("repos", repo.user.login, repo.name, "issues", number)
        data = _get_data(url)
        return cls(data)


class Pull(UserLinkedModel):
    _keys = ['title']

    @classmethod
    def get_all(cls, repo):
        url = make_url("repos", repo.user.login, repo.name, "pulls")
        data = _get_data(url)
        pulls = [cls(p) for p in data]
        return pulls

    @classmethod
    def get(cls, repo, number):
        url = make_url("repos", repo.user.login, repo.name, "pulls", number)
        data = _get_data(url)
        return cls(data)
