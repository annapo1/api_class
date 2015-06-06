from pubapiutils import Calls
import httplib

calls = Calls()


def test_create_5_folders_positive():
    no_json = 'NoJSON'
    folder_path = '/Shared/test_folder/'
    l = []
    for i in range(5):
        folder_name = 'test_folder%s' % i
        resp = calls.create_folder(folder_name)
        print(resp.json)
        assert resp.status_code == httplib.CREATED
        assert resp.json == no_json
        l.append(folder_name)
    for item in l:
        resp = calls.delete_folder(folder_path=folder_path + item)
        assert resp.status_code == httplib.OK

"""
def test_create_folders_positive():
    no_json = 'NoJSON'
    for i in range(3):
        folder_name = 'test_folder123gtg%s' % i
        resp = calls.create_folder(folder_name)
        assert resp.status_code == httplib.CREATED
        assert resp.json == no_json
"""