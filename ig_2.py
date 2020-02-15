import instaloader
import itertools

L = instaloader.Instaloader()
L.login('musketeers1128@gmail.com', 'EvOu7CR7Iq2V')        # (login)


# find a way to limit downloads!
# eg, only get first 20 tagged posts
# TODO: look into itertools techniques

f = L.get_hashtag_posts('dinela')

for post in itertools.islice(f, 10):
    L.download_post(post, target='#dinela')
