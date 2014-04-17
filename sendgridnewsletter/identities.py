from .base import BaseManager


class IdentityManager(BaseManager):
    url = 'newsletter/identity/{verb}'

    def get_identity(self, title):
        return self.master.call(
            self.get_url(verb='get'), [('identity', title)])

    def all(self):
        data = self.master.call(self.get_url(verb='list'))
        return [x['identity'] for x in data]

    def add(self, title, name, email, address, city, state, zip_code, country):
        data = [
            ('identity', title), ('name', name), ('email', email),
            ('address', address), ('city', city), ('state', state),
            ('zip', zip_code), ('country', country)
        ]

        result = self.master.call(self.get_url(verb='add'), data)

        if 'message' in result:
            if result['message'] == 'success':
                return True

        return False

    def edit(self, title, new_title=None, name=None, email=None, address=None,
             city=None, state=None, zip_code=None, country=None):
        data = [
            ('identity', title), ('newidentity', new_title), ('name', name),
            ('email', email), ('address', address), ('city', city),
            ('state', state), ('zip', zip_code), ('country', country)
        ]

        result = self.master.call(self.get_url(verb='edit'), data)

        if 'message' in result:
            if result['message'] == 'success':
                if new_title:
                    return self.get_identity(new_title)
                else:
                    return self.get_identity(title)

        return False

    def delete(self, title):
        result = self.master.call(
            self.get_url(verb='delete'), [('identity', title)])

        if 'message' in result:
            if result['message'] == 'success':
                return True

        return False
