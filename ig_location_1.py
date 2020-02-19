""" 
(Can find Loc ID in web URL on Instagram location page)

Popular Location IDS in LA:
212999109 - Los Angeles
1865514327051885 - DTLA
495901727445891 - DTLA

 """

import instaloader

L = instaloader.Instaloader()

L.login('musketeers1128@gmail.com', 'EvOu7CR7Iq2V')

L.download_location(212999109,
                    max_count=30,
                    # filter by specific hashtag in post's caption
                    post_filter=lambda post: "food" in post.caption_hashtags,
                    fast_update=True)
