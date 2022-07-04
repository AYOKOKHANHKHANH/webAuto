import unittest
# from tests.loginTest import LoginTest
from tests.Contact.addContactTest import AddContact
from tests.Group.createGroupTest import CreateGroup
from tests.Chat.chatTest import ChatTest
from tests.Login.loginAnonymous import LoginAnonymousTest
if __name__ == '__main__':
    # get all tests
    # login = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    add_contact = unittest.TestLoader().loadTestsFromTestCase(AddContact)
    create_group = unittest.TestLoader().loadTestsFromTestCase(CreateGroup)
    chat_test = unittest.TestLoader().loadTestsFromTestCase(ChatTest)
    login_anonymous_test = unittest.TestLoader().loadTestsFromTestCase(LoginAnonymousTest)

    # create a tests suite
    test_suite = unittest.TestSuite([chat_test])

    # run the suite
    unittest.TextTestRunner().run(test_suite)