import mox

from unittest import TestCase

from sendgridnewsletter.client import SendGridMarketing
from sendgridnewsletter.schedules import ScheduleManager


class ScheduleManagerTest(TestCase):
    def setUp(self):
        self.schedule_manager = ScheduleManager(SendGridMarketing('', ''))
        self.mock = mox.Mox()

    def tearDown(self):
        self.mock.UnsetStubs()

    def test_all(self):
        pass

    def test_add(self):
        pass

    def test_add_no_at_no_after(self):
        pass

    def test_add_at_and_after(self):
        pass

    def test_remove(self):
        pass
