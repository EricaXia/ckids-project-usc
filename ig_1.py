import instaloader

# Get instance
L = instaloader.Instaloader()

# Optionally, login or load session
L.login('musketeers1128@gmail.com', 'EvOu7CR7Iq2V')        # (login)
# L.interactive_login(USER)      # (ask password on terminal)
# L.load_session_from_file(USER)  # (load session created w/
# #  `instaloader -l USERNAME`)

# need to set limit on how many posts are downloaded!
# for post in L.get_hashtag_posts('eatla'):
#     # post is an instance of instaloader.Post
#     L.download_post(post, target='#eatla')

L.download_hashtag('eatla', max_count=10)
