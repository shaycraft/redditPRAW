import praw
from config import *

redditOld = praw.Reddit(client_id=REDDIT_CONFIG['source']['client_id'],
                        client_secret=REDDIT_CONFIG['source']['client_secret'],
                        user_agent='user agent here',
                        username=REDDIT_CONFIG['source']['username'],
                        password=REDDIT_CONFIG['source']['password'])

reddit = praw.Reddit(client_id=REDDIT_CONFIG['destination']['client_id'],
                     client_secret=REDDIT_CONFIG['destination']['client_secret'],
                     user_agent='user agent here',
                     username=REDDIT_CONFIG['destination']['username'],
                     password=REDDIT_CONFIG['destination']['password'])

bd = reddit.multireddit(REDDIT_CONFIG['source']['username'], 'multi_name_here')
bdOld = redditOld.multireddit(REDDIT_CONFIG['destination']['username'], 'dest_multi_name_here')


failed_subs = []
failed_multiadd = []
for item in bdOld.subreddits:
    try:
        print 'Subscribing to ' + item.display_name
        reddit.subreddit(item.display_name).subscribe()
    except Exception as err:
        print 'failed subscribe to ' + item.display_name
        failed_subs.append(item)
    try:
        print 'Adding ' + item.display_name + 'to bd multi in new'
        bd.add(item)
    except Exception as err:
        print err

print 'failed multi add = '
print failed_multiadd

print 'failed subs: '
print failed_subs

