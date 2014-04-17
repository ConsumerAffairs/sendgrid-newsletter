import mox

from unittest import TestCase

from sendgridnewsletter.client import SendGridMarketing
from sendgridnewsletter.newsletters import NewsletterManager


class NewsletterManagerTest(TestCase):
    def setUp(self):
        self.newsletter_manager = NewsletterManager(SendGridMarketing('', ''))
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
