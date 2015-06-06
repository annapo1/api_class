import requests
import json
from ConfigParser import SafeConfigParser


def create_folder(folder_name, path=None, domain=None, method=None, content_type=None, accept=None,
                  username=None, password=None):
    if domain is None:
        domain = 'https://istepanko.qa-egnyte.com'
    if method is None:
        method = 'POST'
    if content_type is None:
        content_type = 'application/json'
    if accept is None:
        accept = 'application/json'
    if username is None:
        username = 'istepanko'
    if password is None:
        password = 'egnyte4you'
    if path is None:
        path = '/Shared/test_folder/'

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


def delete_folder(folder_path, domain=None, method=None, content_type=None, accept=None,
                  username=None, password=None):
    if domain is None:
        domain = 'https://istepanko.qa-egnyte.com'
    if method is None:
        method = 'DELETE'
    if content_type is None:
        content_type = 'application/json'
    if accept is None:
        accept = 'application/json'
    if username is None:
        username = 'istepanko'
    if password is None:
        password = 'egnyte4you'

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