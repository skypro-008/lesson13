import unittest

import requests as requests
from task import username, repository_name


class TestCase(unittest.TestCase):
    def test_requirements_file(self):
        url = f"https://raw.githubusercontent.com/{username}/{repository_name}/main/README.md"
        resp = requests.get(url=url)
        self.assertEqual(resp.status_code, 200, msg="Файла README.md нет в репозитории, в ветке main.")