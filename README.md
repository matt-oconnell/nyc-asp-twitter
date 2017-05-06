# nyc-asp-twitter
Retrieve NYC Alt-Side Parking Updates from Twitter (modified for a simple Heroku deployment)

This will setup a single endpoint that provides a JSON array composed of objects that contain 2 keys:

`suspended_dates` is an array of time deltas (`-1` = yesterday, `0` = today, `1` = tomorrow, etc.)

`text` is the text of the tweet

Example:

```json
{
  "suspended_dates": [0], 
  "text": "#NYCASP rules are suspended today, May 8."
},
{
  "suspended_dates": [0, 1], 
  "text": "#NYCASP rules are suspended today May 7 and tomorrow, May 8."
},
{
  "suspended_dates": [], 
  "text": "#NYCASP rules are in effect today, May 6."
}, 
```

# Setup

Set up a developer account on Twitter.
Add a new application.

run `python helper.py` and enter `client_id` and `client_secret`

Set the returned tokens to be environment variables.

Required Env variables: 
- CONSUMER_KEY
- CONSUMER_SECRET
- ACCESS_TOKEN_KEY
- ACCESS_TOKEN_SECRET
