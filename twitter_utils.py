import twitter
import re
import os

if not os.environ.get('CONSUMER_KEY'):
    execfile('keys.py')

api = twitter.Api(consumer_key=os.environ.get('CONSUMER_KEY'),
                  consumer_secret=os.environ.get('CONSUMER_SECRET'),
                  access_token_key=os.environ.get('ACCESS_TOKEN_KEY'),
                  access_token_secret=os.environ.get('ACCESS_TOKEN_SECRET')
                  )


def getSuspendedDates(str):
    if not 'uspended' in str:
        return []
    return re.findall(r'\w*.?\s\d\d*', str)


def getParkingTweets():
    statuses = api.GetUserTimeline(screen_name='NYCASP')
    output = []
    for status in statuses:
        output.append({
            'text': status.text,
            'suspended_dates': getSuspendedDates(status.text)
        })
    return output
