## Javascript Adapter

### Sample magento store with adapter: http://178.62.113.8/  
### Mockup API is up on: http://104.248.248.147/  
To see the log file for handling events on this sample store, go to http://104.248.248.147/log.txt  
  
#### To set up the store and API on another server, just run the build script (magento_build.sh) in the server. This sets up both the store and the API (on port 5678).  

Link to wiki home: https://github.com/stacc-dasso/Javascript-Adapter/wiki

### Scraper using manual
Requirements:
* Python 3+
* Scrapy library

In project root folder run `scrapy crawl magento`  
To save data to .csv file run `scrapy crawl magento -o items.csv -t csv`

### Test execution
Requirements:
* Python 3+
* Selenium plugin
* Chrome browser

In project test folder run `python ui-tests.py`



