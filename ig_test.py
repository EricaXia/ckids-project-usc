from datetime import datetime
from itertools import dropwhile, takewhile

import instaloader

L = instaloader.Instaloader()

posts = L.get_hashtag_posts('eatla')
# or
# posts = instaloader.Profile.from_username(L.context, PROFILE).get_posts()

SINCE = datetime(2020, 2, 7, 0, 0, 0)
UNTIL = datetime(2020, 2, 8, 0, 0, 0)

for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, posts)):
    print(post.date)
    L.download_post(post, '#eatla')
