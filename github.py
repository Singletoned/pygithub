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


class GettableModel(BaseModel):
    @classmethod
    def get_all(cls, *args, **kwargs):
        url = cls._get_all_url(*args, **kwargs)
        data = _get_data(url)
        repos = [cls(i) for i in data]
        return repos

    @classmethod
    def get(cls, *args, **kwargs):
        url = cls._get_url(*args, **kwargs)
        data = _get_data(url)
        return cls(data)


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


class Repo(GettableModel, UserOwnedModel):
    _keys = ['name', 'git_url', 'html_url', 'owner']

    @staticmethod
    def _get_all_url(user):
        return make_url("users", user.login, "repos")

    @staticmethod
    def _get_url(user, name):
        return make_url("repos", user.login, name)

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


class Issue(GettableModel, UserLinkedModel):
    _keys = ['title']

    @staticmethod
    def _get_all_url(repo):
        return make_url("repos", repo.user.login, repo.name, "issues")

    @staticmethod
    def _get_url(repo, number):
        return make_url("repos", repo.user.login, repo.name, "issues", number)


class Pull(GettableModel, UserLinkedModel):
    _keys = ['title']

    @staticmethod
    def _get_all_url(repo):
        return make_url("repos", repo.user.login, repo.name, "pulls")

    @staticmethod
    def _get_url(repo, number):
        return make_url("repos", repo.user.login, repo.name, "pulls", number)
