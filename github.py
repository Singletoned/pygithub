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
        return json.loads(content)
