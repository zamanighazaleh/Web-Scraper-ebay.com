import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

def search_item_in_website():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    service = Service()
    
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://www.ebay.com/')
    
    search = driver.find_element(By.ID,'gh-ac-box2')
    searchbox = search.find_element(By.ID,'gh-ac')
    searchbox.click()
    searchbox.send_keys('comic books')
    searchbox.send_keys(Keys.ENTER)

    return driver

def scroll(y,driver):
    time.sleep(1)
    driver.execute_script(f"window.scrollTo(0, {y})")
    time.sleep(2)

def get_links(driver):
    links = []

    products = driver.find_elements(By.CSS_SELECTOR,'.s-item__link')
    for p in products:
        link = p.get_attribute('href')
        links.append(link)
        
    return links

def extract_and_scroll(driver):
    data = []
    links = get_links(driver)

    for i in range(len(links)):
        driver.get(links[i])
        
        #for i in range(1,8):
        #    scroll(i*500,driver)

        try:
            p = driver.find_element(By.CSS_SELECTOR,'.x-price-primary')
            price = p.find_element(By.CSS_SELECTOR,'.ux-textspans')
            price_text = price.get_attribute('innerHTML')
        except:
            price_text = "-"
        

        try:
            t = driver.find_element(By.CSS_SELECTOR,'.vim.x-item-title')
            ti= t.find_element(By.CSS_SELECTOR,'.x-item-title__mainTitle')
            title = ti.find_element(By.CSS_SELECTOR,'.ux-textspans.ux-textspans--BOLD')
            title_text = title.get_attribute('innerHTML')
        except:
            title_text = "-"
        
        data.append([title_text,price_text,links[i]])
    
    df = pd.DataFrame(data,columns=['title','price','link'])
    
    return df        
        

def scraper():
    driver = search_item_in_website()
    df = extract_and_scroll(driver)
    df.to_csv('comic books.csv')
        
       
scraper()
