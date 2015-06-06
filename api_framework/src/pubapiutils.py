import requests
import json
from ConfigParser import SafeConfigParser
import os
import inspect
from random import randint


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
                      username=None, password=None, print_call=True):
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
        url = '%s%s%s/%s' % (domain, endpoint, path, folder_name)
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

        if print_call:
            header_string = ''
            for key in headers:
                header_string += '-H "%s: %s" ' % (key, headers[key])
            print('\n*TESTCASE: %s, API Call: Create Folder*' % inspect.stack()[1][3])
            print('\nCurl is:\n curl %s "%s" -d \'%s\' -u%s:%s -X %s' % (header_string, url, data, username, password,
                                                                       method))
            print('HTTP Code: %s' % r.status_code)
            print('\nJSON response is:\n %s' % json_resp)

        r.json = json_resp
        return r

    def delete_folder(self, folder_path, domain=None, method=None, content_type=None, accept=None,
                      username=None, password=None, print_call=True):
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

        if print_call:
            header_string = ''
            for key in headers:
                header_string += '-H "%s: %s" ' % (key, headers[key])
            print('\n*TESTCASE: %s, API Call: Delete Folder*' % inspect.stack()[1][3])
            print('\nCurl is:\n curl %s "%s" -u%s:%s -X %s' % (header_string, url, username, password, method))
            print('HTTP Code: %s' % r.status_code)
            print('\nJSON response is:\n %s' % json_resp)

        r.json = json_resp
        return r

    def set_perms(self, folder_path, users, permission, domain=None, method=None, content_type=None, accept=None,
                  username=None, password=None, print_call=True):
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

        endpoint = '/public-api/v1/perms/folder'
        url = '%s%s%s' % (domain, endpoint, folder_path)
        headers = dict()
        headers['Content-Type'] = content_type
        headers['Accept'] = accept
        data = dict()
        data['users'] = []
        data['permission'] = permission
        if type(users) == list:
            for user in users:
                data['users'].append(user)
        else:
            data['users'].append(users)
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

        if print_call:
            header_string = ''
            for key in headers:
                header_string += '-H "%s: %s" ' % (key, headers[key])
            print('\n*TESTCASE: %s, API Call: Set Perms*' % inspect.stack()[1][3])
            print('\nCurl is:\n curl %s "%s" -d \'%s\' -u%s:%s -X %s' % (header_string, url, data, username, password,
                                                                         method))
            print('HTTP Code: %s' % r.status_code)
            print('\nJSON response is:\n %s' % json_resp)

        r.json = json_resp
        return r

    def list_perms(self, folder_path, users, domain=None, method=None, content_type=None, accept=None,
                   username=None, password=None, print_call=True):
        if domain is None:
            domain = self.config.domain
        if method is None:
            method = 'GET'
        if content_type is None:
            content_type = 'application/json'
        if accept is None:
            accept = 'application/json'
        if username is None:
            username = self.config.admin_login
        if password is None:
            password = self.config.password

        endpoint = '/public-api/v1/perms/folder'
        url = '%s%s%s' % (domain, endpoint, folder_path)
        headers = dict()
        headers['Content-Type'] = content_type
        headers['Accept'] = accept

        url += '?users=%s' % users

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

        if print_call:
            header_string = ''
            for key in headers:
                header_string += '-H "%s: %s" ' % (key, headers[key])
            print('\n*TESTCASE: %s, API Call: List Perms*' % inspect.stack()[1][3])
            print('\nCurl is:\n curl %s "%s" -u%s:%s -X %s' % (header_string, url, username, password, method))
            print('HTTP Code: %s' % r.status_code)
            print('\nJSON response is:\n %s' % json_resp)

        r.json = json_resp
        return r


class Utils:
    def __init__(self):
        self.config = Config()

    @staticmethod
    def random_name():
        return 'test_name%s' % randint(1000000, 9999999)