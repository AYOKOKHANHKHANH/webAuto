import unittest
from tests.loginTest import LoginTest
from tests.addContactTest import AddContact

if __name__ == '__main__':
    # get all tests
    login = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    add_contact = unittest.TestLoader().loadTestsFromTestCase(AddContact)

    # create a tests suite
    test_suite = unittest.TestSuite([add_contact])

    # run the suite
    unittest.TextTestRunner().run(test_suite)

