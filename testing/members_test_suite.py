import unittest
from starlette.testclient import TestClient

from main import app
from schemas.member_sh import member_schema

'''
Reference Material
https://fastapi.tiangolo.com/tutorial/testing/
'''

class members_test_suite(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)
        pass

    def test_1_save_valid_member(self):
        new_user = member_schema(
            charges_id=1,
            fullname="margarita Fierro Najera",
            blood_type="A+",
            email="margarita.fierro796@gmail.com",
            password="pass",
            address="address",
            phone_number="phonenumber",
            image="",
            birthdate="1993-07-04",
            is_active=True
            )

        response = self.client.post("/members"
                                    , headers={"Content-Type": "application/json"}
                                    , json=dict(new_user))
        print(response.content)
        self.assertEqual(response.content, '{"message":"New member has been created"}')

    def test_2_retrieve_all_members(self):
        response = self.client.get("/members")
        print(response.content)
        self.assertEqual(response.status_code, 200)

    def test_3_retrieve_member_by_email_and_password(self):
        user = {
            "email": "margarita.fierro796@gmail.com",
            "password": "pass"
        }

        response = self.client.post("/members/login",
                                json=user,
                                headers={"Content-Type": "application/json"})
        print(response)
    # end class