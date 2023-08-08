# Web-Scraper-ebay.com
Download a ChromeDriver that is compatible with your chrome version from [here](https://chromedriver.chromium.org/downloads) and put it in the same folder with the code.

I have used “headless” as the option for webdriver to make the code run faster. If you want to see the scraping process, uncomment two lines of scroll in `extract_and_scroll()` function and  use this line of code in `search_item_in_website()` function to define the driver:
`driver = webdriver.Chrome(service=service)`
# Requirements
Selenium

ChromeDriver
