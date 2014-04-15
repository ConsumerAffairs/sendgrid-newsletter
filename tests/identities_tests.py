import mox

from unittest import TestCase

from sendgridnewsletter.client import SendGridMarketing
from sendgridnewsletter.identities import IdentityManager


class IdentityManagerTest(TestCase):
    def setUp(self):
        self.identities_manager = IdentityManager(SendGridMarketing('', ''))
        self.mock = mox.Mox()

    def tearDown(self):
        self.mock.UnsetStubs()

    def test_all(self):
        pass

    def test_add(self):
        pass

    def test_delete(self):
        pass

    def test_edit(self):
        pass
