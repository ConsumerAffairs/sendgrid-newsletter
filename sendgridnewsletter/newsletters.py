from .base import BaseManager
from .exceptions import DoesNotExist


class NewsletterManager(BaseManager):
    url = 'newsletter/{verb}'

    def all(self):
        return self.master.call(self.get_url(verb='list'))

    def exists(self, name):
        try:
            self.master.call(
                self.get_url(verb='get'), [('name', name)])
            return True
        except Exception:
            return False

    def get_newsletter(self, name):
        if self.exists(name):
            return self.master.call(
                self.get_url(verb='get'), [('name', name)])
        else:
            raise DoesNotExist(
                "'{name}' newsletter does not exist".format(name=name))

    def add(self, identity, name, subject, text, html):
        data = [
            ('identity', identity), ('name', name), ('subject', subject),
            ('text', text), ('html', html)
        ]

        result = self.master.call(self.get_url(verb='add'), data)

        if 'message' in result:
            if result['message'] == 'success':
                return self.get_newsletter(name)

        return False

    def edit(self, name, identity=None, new_name=None, subject=None, text=None,
             html=None):
        data = [
            ('identity', identity), ('name', name), ('newname', new_name),
            ('subject', subject), ('text', text), ('html', html)
        ]

        result = self.master.call(self.get_url(verb='edit'), data)

        if 'message' in result:
            if result['message'] == 'success':
                if new_name:
                    return self.get_newsletter(new_name)
                else:
                    return self.get_newsletter(name)

        return False

    def delete(self, name):
        result = self.master.call(
            self.get_url(verb='delete'), [('name', name)])

        if 'message' in result:
            if result['message'] == 'success':
                return True

        return False
