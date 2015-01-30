# Scrapy settings for yelp project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'yelp'

SPIDER_MODULES = ['yelp.spiders']
NEWSPIDER_MODULE = 'yelp.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'yelp (+http://www.yourdomain.com)'
