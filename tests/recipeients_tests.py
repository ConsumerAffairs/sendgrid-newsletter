import mox

from unittest import TestCase

from sendgridnewsletter.client import SendGridMarketing
from sendgridnewsletter.recipients import RecipientsManager


class RecipientsManagerTest(TestCase):
    def setUp(self):
        self.recipients_manager = RecipientsManager(SendGridMarketing('', ''))
        self.mock = mox.Mox()

    def tearDown(self):
        self.mock.UnsetStubs()

    def test_all(self):
        pass

    def test_add(self):
        pass

    def test_remove_list(self):
        pass
