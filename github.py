# -*- coding: utf-8 -*-

import json

import requests
import werkzeug

url = werkzeug.Href("https://api.github.com/")

class Github(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        response = requests.get(
            url(),
            auth=(self.username, self.password))

    @property
    def user(self):
        response = requests.get(
            url("users", self.username))
        content = response.content
        data = json.loads(content)
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
        response = requests.get(
            url("users", self.login, "repos"))
        content = response.content
        data = json.loads(content)
        return data

    def get_repo(self, name):
        response = requests.get(
            url("repos", self.login, name))
        content = response.content
        data = json.loads(content)
        return Repo(data)


class Repo(BaseModel):
    _keys = ['name', 'git_url', 'html_url', 'owner']

    @property
    def user(self):
        response = requests.get(
            url("users", self.owner['login']))
        content = response.content
        data = json.loads(content)
        user = User(data)
        return user

    @property
    def issues(self):
        response = requests.get(
            url("repos", self.user.login, self.name, "issues"))
        content = response.content
        data = json.loads(content)
        return data

    def get_issue(self, number):
        response = requests.get(
            url("repos", self.user.login, self.name, "issues", number))
        content = response.content
        data = json.loads(content)
        return Issue(data)
        return data


class Issue(BaseModel):
    _keys = ['title']
