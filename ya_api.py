import os
import requests
import unittest
from dotenv import load_dotenv


def create_ya_disk_dir():
    load_dotenv()
    token = os.environ["token"]
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    path = 'New_dir6'
    headers = {'Authorization': token}
    params = {'path': path, 'overwrite': True}
    response = requests.put(url, headers=headers, params=params)
    return response


class TestYaDisk(unittest.TestCase):
    response = create_ya_disk_dir()
    resp = response.json()
    resp_code = response.status_code

    def test_check_create_dir(self):
        check_resp = 0
        message = ''
        if 'href' in self.resp.keys():
            check_resp = 1
        if 'message' in self.resp.keys():
            message = self.resp['message']
        self.assertTrue(check_resp, message)

    @unittest.expectedFailure
    def test_check_fail_dir(self):
        check_resp = 0
        message = 'Dir was created'
        if 'href' in self.resp.keys():
            check_resp = 1
        if 'message' in self.resp.keys():
            message = self.resp['message']
        self.assertFalse(check_resp, message)

    def test_check_status(self):
        self.assertEqual(self.resp_code, 201, 'Code not 201 Created')


if __name__ == '__main__':
    unittest.main(verbosity=2)
