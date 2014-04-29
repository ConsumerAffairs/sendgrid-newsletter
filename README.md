# sendgrid-newsletter
This is a library to interact with the newsletter api built by sendgrid.



## Quick Usage Example

```python
import sendgridnewsletter.client import SendGridMarketing

sendgrid_username = 'someuser'
sendgrid_password = 'somepass'

client = SendGridMarketing(sendgrid_username, sendgrid_password)

# get all email lists
client.lists.all()

# create a list
client.lists.add('listname')

# delete a list
client.lists.delete('listname')

# rename a list
client.lists.rename('oldname', 'newname')

# get a specific list
list = client.lists.get_list('somename')

# get all emails in a list
emails = list.emails()

# check for specific email in list
list.has_email('name@example.com')

# add a single email address
list.add_email('name@example.com', 'name')

# add multiple emails
emails = [
    {'email': 'email1@example.com', 'name': 'email name'},
    {'email': 'email2@example.com', 'name': 'name email'}]

list.add_emails(emails)

# delete a specific email
list.delete_email('email@example.com

```

## Features
Attempts to make the API more usable.
