import unittest
from starlette.testclient import TestClient
import httpx

from main import app
from schemas.member_sh import member_schema

'''
Reference Material
https://fastapi.tiangolo.com/tutorial/testing/
'''


class UsersTestCases(unittest.TestCase):

    def test_retrive_all_members(self):
        client = TestClient(app)
        response = client.get("/members")
        print(response.content)
        self.assertEquals(response.status_code, 200)
        pass

    def test_save_new_member(self):
        client = TestClient(app)

        # create new user values
        new_user = member_schema(charges_id=3,
                                 fullname="Angel Esteban Fierro Najera",
                                 blood_type="A+",
                                 email="angel.fierro796@gmail.com",
                                 password="pass",
                                 address="address",
                                 phone_number="phonenumber",
                                 image="",
                                 birthdate="1993-07-04",
                                 is_active=True)

        response = client.post("/members"
                               , headers={"Content-Type": "application/json"}
                               , json=dict(new_user))
        print(response)
        pass

    pass
    # End test suite
