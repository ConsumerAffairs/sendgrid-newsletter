import urllib

from .base import BaseManager, BaseObject


class ListManager(BaseManager):
    url = 'newsletter/lists/{verb}'

    def all(self):
        data = self.master.call(self.get_url(verb='get'))
        return [x['list'] for x in data]

    def exists(self, name):
        data = self.master.call(
            self.get_url(verb='get'), {'list': name})

        if data[0]['list'] == name:
            return True

        return False

    def get_list(self, name):
        if not self.exists(name):
            raise Exception(
                "'{name}' list does not exist".format(name=name))

        return List(self.master, name)

    def add(self, name, email_name='email'):
        data = self.master.call(
            self.get_url(verb='add'),
            {'list': name, 'name': email_name})

        if 'message' in data:
            status = data['message']
            if status == 'success':
                return True

        return False

    def delete(self, name):
        data = self.master.call(
            self.get_url(verb='delete'), {'list': name})

        if 'message' in data:
            status = data['message']
            if status == 'success':
                return True

        return False

    def rename(self, old_name, new_name):
        if not self.exists(old_name):
            raise Exception(
                "'{name}' list does not exist".format(name=old_name))

        data = self.master.call(
            self.get_url(verb='edit'),
            {'list': old_name, 'newlist': new_name})

        if 'message' in data:
            if data['message'] == 'success':
                return True

        return False


class List(BaseObject):
    url = 'newsletter/lists/email/{verb}'

    def __init__(self, master, list_name):
        self.master = master
        self.list_name = list_name
        self.payload = {}
        self.payload['list'] = self.list_name

    def emails(self):
        return self.master.call(
            self.get_url(verb='get'), self.payload)

    def has_email(self, email):
        self.payload['email'] = email

        data = self.master.call(
            self.get_url(verb='get'), self.payload)

        if data:
            return True

        return False

    def add_email(self, email, name):
        self.payload['data'] = self.to_json({'email': email, 'name': name})

        data = self.master.call(
            self.get_url(verb='add'), self.payload)

        if 'inserted' in data:
            return True

        return False

    def add_emails(self, data):
        json_data = map(self.to_json, data)
        collected_data = "&data[]=".join(map(urllib.quote, json_data))
        final_data = "data[]=" + collected_data
        data = self.master.call(
            self.get_url(verb='add'), self.payload,
            data_override=final_data)

        if 'inserted' in data:
            return True

        return False

    def delete_email(self, email):
        self.payload['email'] = email

        data = self.master.call(
            self.get_url(verb='delete'), self.payload)

        if 'removed' in data:
            return True

        return False
