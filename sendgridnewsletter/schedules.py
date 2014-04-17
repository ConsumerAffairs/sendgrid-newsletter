from .base import BaseManager


class ScheduleManager(BaseManager):
    url = 'newsletter/schedule/{verb}'

    def get(self, newsletter_name):
        return self.master.call(
            self.get_url(verb='get'), [('name', newsletter_name)])

    def add(self, newsletter_name, at=None, after=None):
        if at and after:
            raise Exception('at and after cannot both be set')

        if not at and not after:
            raise Exception('either at or after must be set')

        payload = []
        payload.append(('name', newsletter_name))
        payload.append(('at', at.strftime("%Y-%m-%d %H:%M:%S")))
        payload.append(('after', after))

        result = self.master.call(self.get_url(verb='add'), payload)

        if 'message' in result:
            if result['message'] == 'success':
                return True

        return False

    def remove(self, newsletter_name):
        result = self.master.call(
            self.get_url(verb='delete'), [('name', newsletter_name)])

        if 'message' in result:
            if result['message'] == 'success':
                return True

        return False
