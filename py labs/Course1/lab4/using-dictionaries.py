emails = {}

emails['ashley'] = 'ashley@example.com'
emails['craig'] = 'craig@example.com'
emails['elizabeth'] = 'elizabeth@example.com'

del emails['craig']

emails['dalton'] = 'dalton@example.com'

users = list(emails.keys())
email_list = list(emails.values())

pairs = list(emails.items())


#print(pairs)
