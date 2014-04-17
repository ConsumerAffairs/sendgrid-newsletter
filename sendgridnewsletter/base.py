import json

from .exceptions import ImproperlyConfigured


class BaseObject(object):
    url = None

    def to_json(self, dictionary):
        return json.dumps(dictionary)

    def get_url(self, **kwargs):
        if not self.url:
            raise ImproperlyConfigured(
                "'{klass}' needs a url set".format(klass=self.__class__))

        return self.url.format(**kwargs)


class BaseManager(BaseObject):
    def __init__(self, master):
        self.master = master
