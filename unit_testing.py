import unittest
from starlette.testclient import TestClient
import httpx

from main import app


class UsersTestCases(unittest.TestCase):

    def test_retrive_all_members(self):
        client = TestClient(app)
        response = client.get("/members")
        print(response.content)
        self.assertEquals(response.status_code, 200)
        pass
        #end test
    
    # End test suite


