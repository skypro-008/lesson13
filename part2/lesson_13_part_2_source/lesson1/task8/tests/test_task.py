import unittest

import requests as requests
from task import username, repository_name, pull_request_number


class TestCase(unittest.TestCase):
    def test_requirements_file(self):
        url = f"https://github.com/{username}/{repository_name}/pull/{pull_request_number}"
        resp = requests.get(url=url)
        self.assertEqual(resp.status_code, 200, msg=f"Pull реквеста с номером {pull_request_number} нет")