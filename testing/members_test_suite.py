import unittest
from starlette.testclient import TestClient

from main import app

'''
Reference Material
https://fastapi.tiangolo.com/tutorial/testing/
'''

class members_test_suite(unittest.TestCase):

    def test_1_retrieve_all_members(self):
        client = TestClient(app)
        response = client.get("/members")
        print(response.content)
        self.assertEquals(response.status_code, 200)
    pass
    # end class