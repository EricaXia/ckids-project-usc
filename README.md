# Web Scraping Instagram Posts

## Workflow:
1. Download and make use of [Instaloader](https://instaloader.github.io/) Python tool. Instaloader has two options for downloading:
  - Command line utility (I primarily used this)
  - As an imported Python package
  
2. Install the tool [as per instructions](https://instaloader.github.io/installation.html#install). If you are using Windows, you can download the standalone program [here](https://github.com/instaloader/instaloader/releases).

3. You can verify if it was installed properly by running `instaloader --help` within your command line terminal.

4. Posts can be downloaded by specifying options to the command line tool. For instance, typing the command 

`instaloader --login="YOUR-INSTAGRAM-EMAIL-HERE" --password="YOUR-INSTAGRAM-PASSWORD" --no-videos --geotags --comments --no-compress-json --post-filter="datetime(2020, 2, 1) <= date_utc <= datetime(2020, 4, 1)" --count=5000 --request-timeout=300 #burger`

Will download all posts containing the hashtag "#burger" within the date range 2/1/2020 to 4/1/2020 with an upper limit of 5000 posts.

5. For more detailed instructions on how to use the package, see the instaloader documentation on their website.

6. To clean and transform the raw data (in JPG, JSON, and TXT formats) to a more tidy CSV, see the examples on the Jupyter notebooks in this repo. I made use of packages such as Python pandas, numpy, json, and more to transform the data.


## Documentation
Please see the [Instaloader website](https://instaloader.github.io/index.html) for the full documentation and usage guide.
