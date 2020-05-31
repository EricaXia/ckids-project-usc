# Web Scraping Instagram Posts

## Workflow:
1. Download and make use of [Instaloader](https://instaloader.github.io/) Python tool. Instaloader has two options for downloading:
  - Command line utility (I primarily used this)
  - As an imported Python package
2. Install the tool [as per instructions](https://instaloader.github.io/installation.html#install). If you are using Windows, you can download the standalone program [here](https://github.com/instaloader/instaloader/releases).
3. You can verify if it was installed properly by running `instaloader --help` within command line terminal.
3. Posts can be downloaded by specifying options to the command line tool. For instance, 
`instaloader --login="YOUR-INSTAGRAM-EMAIL-HERE" --password="YOUR-INSTAGRAM-PASSWORD" --no-videos --geotags --comments --no-compress-json --post-filter="datetime(2020, 2, 1) <= date_utc <= datetime(2020, 4, 1)" --count=5000 --request-timeout=300 #burger`

Will download all posts containing the hashtag "#burger" within the date range 2/1/2020 to 4/1/2020 with an upper limit of 5000 posts.



## Documentation
Please see the Instaloader website for the full documentation and usage guide.
