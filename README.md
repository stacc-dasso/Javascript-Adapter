## Javascript Adapter
Sample magento store with adapter: http://178.62.113.8/
Mockup API is up on: http://104.248.248.147/
From the store, all search events and clicking on an item events are sent to API.

Link to wiki home: https://github.com/stacc-dasso/Javascript-Adapter/wiki

### Scraper using manual
Requirements:
* Python 3+
* Scrapy library

In project root folder run `scrapy crawl magento`  
To save data to .csv file run `scrapy crawl magento -o items.csv -t csv`
