import mox

from unittest import TestCase

from sendgridnewsletter.client import SendGridMarketing
from sendgridnewsletter.lists import List, ListManager


class ListManagerTest(TestCase):
    def setUp(self):
        self.list_manager = ListManager(SendGridMarketing('', ''))
        self.mock = mox.Mox()

    def tearDown(self):
        self.mock.UnsetStubs()

    def test_all(self):
        self.mock.StubOutWithMock(SendGridMarketing, 'call')
        self.list_manager.master.call(
            'newsletter/lists/get',
            [('list', 'data')]).AndReturn([{'list': 'data'}])

        self.mock.ReplayAll()
        result = self.list_manager.exists('data')
        self.mock.VerifyAll()

        self.assertTrue(result)

    def test_delete(self):
        self.mock.StubOutWithMock(SendGridMarketing, 'call')
        self.list_manager.master.call(
            'newsletter/lists/delete',
            [('list', 'data')]).AndReturn({'message': 'success'})

        self.mock.ReplayAll()
        result = self.list_manager.delete('data')
        self.mock.VerifyAll()

        self.assertTrue(result)

    def test_delete_error(self):
        self.mock.StubOutWithMock(SendGridMarketing, 'call')
        self.list_manager.master.call(
            'newsletter/lists/delete',
            [('list', 'data')]).AndReturn({'error': 'fail'})

        self.mock.ReplayAll()
        result = self.list_manager.delete('data')
        self.mock.VerifyAll()

        self.assertFalse(result)

    def test_rename(self):
        data = [('list', 'list1'), ('newlist', 'list2')]

        self.mock.StubOutWithMock(ListManager, 'exists')
        self.mock.StubOutWithMock(SendGridMarketing, 'call')

        self.list_manager.exists('list1').AndReturn(True)
        self.list_manager.master.call(
            'newsletter/lists/edit', data).AndReturn({'message': 'success'})

        self.mock.ReplayAll()
        result = self.list_manager.rename('list1', 'list2')
        self.mock.VerifyAll()

        self.assertTrue(result)

    def test_rename_error(self):
        data = [('list', 'list1'), ('newlist', 'list2')]
        self.mock.StubOutWithMock(ListManager, 'exists')
        self.mock.StubOutWithMock(SendGridMarketing, 'call')

        self.list_manager.exists('list1').AndReturn(True)
        self.list_manager.master.call(
            'newsletter/lists/edit', data).AndReturn({'error': 'fail'})

        self.mock.ReplayAll()
        result = self.list_manager.rename('list1', 'list2')
        self.mock.VerifyAll()

        self.assertFalse(result)

    def test_rename_no_list(self):
        self.mock.StubOutWithMock(ListManager, 'exists')
        self.list_manager.exists('list1').AndReturn(False)

        self.mock.ReplayAll()
        self.assertRaises(
            Exception, self.list_manager.rename, 'list1', 'list2')
        self.mock.VerifyAll()
