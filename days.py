oath_token='#Token goes in here.'
my_birth_day = '2013-09-21T00:00:00+0000'
 
from facepy import GraphAPI
from dateutil import parser
import json
import random
graph = GraphAPI(oath_token)
 
my_facebook_id = graph.get('me')['id'].encode('utf-8')
my_birth_date = parser.parse(my_birth_day)
fetchMoreFeeds = True
feedLink = "me/feed"
posts = []
bD_strings = set([ "happy birthday"])
thank_you_notes = [
    " Thank you for your birthday greeting :)",
    "Your birthday greeting was nice. Thank you :)",
    "Thank you :)",
    "Thank you all for remembering such a special day for me",
 
]
 
def getPost(feeds):
    """
    Function to get individual post from the feeds,
    It adds the post to an array @posts if
             * it is addressed to the user
             * after the birthday until now
             * user didn't commented already
             * contains wishing words like happy, birthday
    """
    global fetchMoreFeeds
    for feed in feeds['data']:
        if not feed.has_key("message"):
            continue
        if feed['from']['id'].encode('utf-8') == my_facebook_id:
            continue
        created_date = parser.parse(feed['created_time'])
        if created_date.__lt__(my_birth_date):
            fetchMoreFeeds = False
            return
        if feed['to']['data'][0]['id'].encode('utf-8') != my_facebook_id:
            continue
        message = feed['message'].encode('utf-8').lower()
        if bD_strings.intersection(set(message.split())).__len__() > 0:
            post = {}
            post['id'] = feed['id']
            post['url'] = feed['actions'][0]['link']
            post['sender_name'] = feed['from']['name'].encode('utf-8')
            post['sender_id'] = feed['from']['id'].encode('utf-8')
            posts.append(post)
 
    feedLink = feeds['paging']['next'].replace('https://graph.facebook.com/', '')
    return feedLink
 
while fetchMoreFeeds:
    feeds = graph.get(feedLink)
    feedLink = getPost(feeds)
 
for post in posts:
    post_link = str(post['id']) + '/comments'
    thank_note  = thank_you_notes[random.randint(0, len(thank_you_notes) -1) ]
    graph.post(post_link, message=thank_note)
    print "Wished %s .." % (post['sender_name'])
