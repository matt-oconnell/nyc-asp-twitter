import twitter
from dateutil import parser
from datetime import datetime
import re
import os

if not os.environ.get('CONSUMER_KEY'):
    execfile('keys.py')

api = twitter.Api(consumer_key=os.environ.get('CONSUMER_KEY'),
                  consumer_secret=os.environ.get('CONSUMER_SECRET'),
                  access_token_key=os.environ.get('ACCESS_TOKEN_KEY'),
                  access_token_secret=os.environ.get('ACCESS_TOKEN_SECRET')
                  )

def getSuspendedDateDeltas(str):
    # if not 'uspended' in str:
    #     return []

    date_deltas = []
    suspended_dates = re.findall(r'\w*.?\s\d\d*', str)

    for date_str in suspended_dates:
        delta = parser.parse(date_str) - datetime.now()
        date_deltas.append(delta.days + 1)
    return date_deltas


def getParkingTweets():
    statuses = api.GetUserTimeline(screen_name='NYCASP')
    output = []
    for status in statuses:
        suspended_dates = getSuspendedDateDeltas(status.text)
        output.append({
            'text': status.text,
            'suspended_dates': suspended_dates
        })
    return output
