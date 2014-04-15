import requests

from .lists import ListManager
from .identities import IdentityManager
from .newsletters import NewsletterManager
from .schedules import ScheduleManager
from .recipients import RecipientsManager


class SendGridMarketing(object):
    def __init__(self, api_user=None, api_key=None):
        if api_user is None or api_key is None:
            raise Exception('You must set api_user and api_key')

        self.api_user = api_user
        self.api_key = api_key
        self.root_url = 'https://api.sendgrid.com/api'

        self.lists = ListManager(self)
        self.identities = IdentityManager(self)
        self.newsletters = NewsletterManager(self)
        self.schedule = ScheduleManager(self)
        self.recipients = RecipientsManager(self)

    def call(self, app, params={}, data_type='json', data_override=None):
        params.update(api_user=self.api_user)
        params.update(api_key=self.api_key)

        url = '{root_url}/{app}.{data_type}'.format(
            root_url=self.root_url, app=app, data_type=data_type)
        if not data_override:
            response = requests.get(url, params=params)
        else:
            url = "{url}?{data}".format(url=url, data=data_override)
            response = requests.get(url, params=params)

        final_result = response.json()
        if 'error' in final_result:
            raise Exception(final_result['error'])

        return final_result
