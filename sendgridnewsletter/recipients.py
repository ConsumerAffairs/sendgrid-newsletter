from .base import BaseManager


class RecipientsManager(BaseManager):
    url = 'newsletter/recipients/{verb}'

    def all(self, newsletter_name):
        data = self.master.call(
            self.get_url(verb='get'), [('name', newsletter_name)])
        return [x['list'] for x in data]

    def add_list(self, newsletter_name, list_name):
        payload = [('name', newsletter_name), ('list', list_name)]
        result = self.master.call(self.get_url(verb='add'), payload)

        if 'message' in result:
            if result['message'] == 'success':
                return True

        return False

    def remove_list(self, newsletter_name, list_name):
        payload = [('name', newsletter_name), ('list', list_name)]
        result = self.master.call(self.get_url(verb='delete'), payload)

        if 'message' in result:
            if result['message'] == 'success':
                return True

        return False
