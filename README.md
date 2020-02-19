# Web Scraping from IG

### Create an Instaloader() object
`loader = Instaloader()`

Functions we can use to scrape:
<br><br>
BY LOCATION
<br>*Note: need IG location ID (see database of IDs in LA)
`loader.download_location(362629379, max_count=30, post_filter=None, fast_update=True)`

BY HASHTAG
<br>
`loader.download_hashtag('food', max_count=30), post_filter=None, fast_update=True)`
<br>
<br>
fast_update set to True so we don't donwload duplicates
<br>TODO: Look into how to modify post_filter argument so we can filter hashtags by location