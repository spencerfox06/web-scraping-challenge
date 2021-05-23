from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
#import pandas as pd
#import tables

def m2m_scrape():
    # scrape mission to mars
    executable_path = ChromeDriverManager().install()
    browser = Browser('chrome', executable_path=executable_path, headless=True)

    # scrape title and teaser
    browser.visit('https://redplanetscience.com/')

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    news_title = soup.find(class_='content_title')
    news_p = soup.find(class_='article_teaser_body')
    
    print(news_title, news_p)

    #scrape featured image
    browser.visit('https://spaceimages-mars.com/')

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    featured_image_url = soup.find('img')['src']

    featured_image_url = 'https://spaceimages-mars.com/image/featured/mars1.jpg'
    
    #print(featured_image_url)

    # #scrape mars facts table and convert from html
    # url = 'https://galaxyfacts-mars.com/'

    # mars_earth_table = pd.read_html(url)
    # #mars_earth_table

    # #place table into pandas dataframe
    # mars_earth_table = tables[0]
    # mars_earth_table

    # scrape hemisphere images
    hemisphere_image_urls = [
    
    {"title": "Cerberus Hemisphere", "img_url": "https://marshemispheres.com/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg"},
    {"title": "Valles Marineris Hemisphere", "img_url": "https://marshemispheres.com/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://marshemispheres.com/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://marshemispheres.com/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg"},
    
    ]

    #print(hemisphere_image_urls)

    browser.quit()

    post = {

        'Latest Mars News': [news_title, news_p],
        'Featured Mars Image': featured_image_url,
        #'Mars Facts': mars_earth_table,
        'Hemisphere Images': hemisphere_image_urls

    }

    return post
