# -*- coding: utf-8 -*-

import json

import requests


class Github(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        response = requests.get(
            'https://api.github.com/',
            auth=(self.username, self.password))

    @property
    def user(self):
        response = requests.get('https://api.github.com/users/%s' % self.username)
        content = response.content
        data = json.loads(content)
        user = User(data)
        return user


class BaseModel(object):
    def __init__(self, data):
        for key in self._keys:
            setattr(self, key, data[key])

class User(BaseModel):
    _keys = ['name', 'email', 'login']

    @property
    def repos(self):
        response = requests.get(
            'https://api.github.com/users/%s/repos' % self.login)
        content = response.content
        data = json.loads(content)
        return data

    def get_repo(self, name):
        response = requests.get(
            'https://api.github.com/repos/%s/%s' % (self.login, name))
        content = response.content
        data = json.loads(content)
        return Repo(data)


class Repo(BaseModel):
    _keys = ['name', 'git_url', 'html_url']
