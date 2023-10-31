import unittest

from main import new_user, hello_world


class UsersTestCases(unittest.TestCase):

    async def test_hello_world_function(self):
        result = await hello_world()
        print(result)

    # End test suite


