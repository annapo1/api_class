import requests
import json
from ConfigParser import SafeConfigParser
import os


class Config:
    def __init__(self):
        self.parser = SafeConfigParser()
        if os.path.isfile('config.ini'):
            self.parser.read('config.ini')
        else:
            print('No config.ini found under root folder.')
        self.domain = self.parser.get('Server', 'url')
        self.admin_login = self.parser.get('Server', 'user')
        self.password = self.parser.get('Server', 'passwd')
        self.puser = self.parser.get('Server', 'puser')
        self.testpath = self.parser.get('Server', 'testpath')


class Calls:
    def __init__(self):
        self.config = Config()

    def create_folder(self, folder_name, path=None, domain=None, method=None, content_type=None, accept=None,
                      username=None, password=None):
        if domain is None:
            domain = self.config.domain
        if method is None:
            method = 'POST'
        if content_type is None:
            content_type = 'application/json'
        if accept is None:
            accept = 'application/json'
        if username is None:
            username = self.config.admin_login
        if password is None:
            password = self.config.password
        if path is None:
            path = self.config.testpath

        endpoint = '/public-api/v1/fs'
        url = '%s%s%s%s' % (domain, endpoint, path, folder_name)
        headers = dict()
        headers['Content-Type'] = content_type
        headers['Accept'] = accept
        data = dict()
        data['action'] = 'add_folder'
        data = json.dumps(data)

        r = requests.request(
            method=method,
            url=url,
            headers=headers,
            data=data,
            auth=(username, password)
        )

        try:
            json_resp = json.loads(r.content)
        except ValueError:
            json_resp = 'NoJSON'

        r.json = json_resp
        return r

    def delete_folder(self, folder_path, domain=None, method=None, content_type=None, accept=None,
                      username=None, password=None):
        if domain is None:
            domain = self.config.domain
        if method is None:
            method = 'DELETE'
        if content_type is None:
            content_type = 'application/json'
        if accept is None:
            accept = 'application/json'
        if username is None:
            username = self.config.admin_login
        if password is None:
            password = self.config.password

        endpoint = '/public-api/v1/fs'
        url = '%s%s%s' % (domain, endpoint, folder_path)
        headers = dict()
        headers['Content-Type'] = content_type
        headers['Accept'] = accept

        r = requests.request(
            method=method,
            url=url,
            headers=headers,
            auth=(username, password)
        )

        try:
            json_resp = json.loads(r.content)
        except ValueError:
            json_resp = 'NoJSON'

        r.json = json_resp
        return r