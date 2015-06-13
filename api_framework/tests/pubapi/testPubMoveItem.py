from pubapiutils import Calls
from pubapiutils import Config
from pubapiutils import Utils
import httplib
from unittest import TestCase


class TestClass(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.no_json = 'NoJSON'
        cls.calls = Calls()
        cls.config = Config()
        cls.utils = Utils()

    def setUp(self):
        self.utils.delete_all_except(['Documents'])

    def test_move_folder_positive(self):
        folder1 = self.utils.random_name()
        folder2 = self.utils.random_name()
        folder2_path = '%s/%s' % (self.config.testpath, folder2)
        folder1_path = '%s/%s' % (self.config.testpath, folder1)
        self.calls.create_folder(folder1)
        self.calls.create_folder(folder2)
        resp = self.calls.move_item(name=folder1, destination=folder2_path)
        assert resp.status_code == httplib.OK
        assert resp.json == self.no_json
        resp = self.calls.list_folders(folder_path=folder2_path)
        assert resp.json['folders'][0]['name'] == folder1
        resp = self.calls.list_folders(folder_path=folder1_path)
        assert resp.status_code == httplib.NOT_FOUND

    def test_move_non_existent_folder(self):
        folder1 = self.utils.random_name()
        folder2 = self.utils.random_name()
        folder1_path = '%s/%s' % (self.config.testpath, folder1)
        self.calls.create_folder(folder1)
        resp = self.calls.move_item(name=folder2, destination=folder1_path, parent_path=self.config.testpath)
        assert resp.status_code == httplib.NOT_FOUND
        assert resp.json['errorMessage'] == "Source path for move doesn't exist"
        
    def test_move_folder_permissions_all(self):
        perms ={'None': 0, 'Viewer': 1, 'Editor': 2, 'Full' = 3, 'Owener' = 4}
        source_folder = self.utils.random_name()
        target_folder = self.utils.random_name()
        source_folder_path = '%s/%s' % (self.config.testpath, source_folder)
        target_folder_path = '%s/%s' % (self.config.testpath, target_folder)
        for perm1 in perms:
            for perm2 in perms:
                self.calls.create_folder(source_folder)
                self.calls.create_folder(target_folder)
                self.calls.set_perms(folder_path=source_folder_path, permission=perm1, users=self.config.puser)
                self.calls.set_perms(folder_path=source_folder_path, permission=perm2, users=self.config.puser)
                resp = self.calls.move_item(name=source_folder, destination=target)
                if perms[perm1] > 2 and perms[perm2] > 1:
                    assert resp.status_code = httplib.OK
                    assert resp.json == self.no_json
                else:
                    assert resp.status_code = httplib.FORBIDDEN
                    assert True
                self.calls.delete_folder(name='', parent_path=self
        
        
