from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

#os.path.basename(r"C:\Users\mihir\Desktop\chromedriver_win32\chromedriver.exe")


browser = webdriver.Chrome("C:/Users/mihir/Desktop/chromedriver_win32/chromedriver.exe")
url = 'http://www.facebook.com/'
browser.get(url)
browser.implicitly_wait(30)



browser.find_element_by_id("email").send_keys("7703965076")
browser.find_element_by_id("pass").send_keys("nidhi98")
browser.set_page_load_timeout(50)
browser.find_element_by_id("loginbutton").click()


browser.set_page_load_timeout(50)

browser.find_element_by_tag_name("body").send_keys(Keys.ESCAPE)
browser.set_page_load_timeout(50)

browser.get("https://www.facebook.com/profile.php?id=100028030908797")


browser.set_page_load_timeout(30)
browser.find_element_by_tag_name("body").send_keys(Keys.ESCAPE)
chrome_options = webdriver.ChromeOptions()
#a = browser.switch_to_alert()
#a.accept()
browser.set_page_load_timeout(30)
#browser.find_element_by_link_text("Photos").click()
browser.get("https://www.facebook.com/profile.php?id=100028030908797&lst=100028030908797%3A100028030908797%3A1536395096&sk=friends&source_ref=pb_friends_tl")
browser.set_page_load_timeout(60)
#webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
browser.find_element_by_tag_name("body").send_keys(Keys.ESCAPE)
########################################################################
browser.set_page_load_timeout(30)#_6a _6b
list =[]
name=[]
list =browser.find_elements_by_xpath("//div[@class='fsl fwb fcb']")
print len(list)
for l in list:
    likes=[]
   
    print l.find_element_by_tag_name("a").text
    name=l.find_element_by_tag_name("a").text
    
    
    browser.implicitly_wait(30)
   
    browser.find_element_by_link_text(l.find_element_by_tag_name("a").text).click()
               
    
    browser.implicitly_wait(30)
                   

    
    browser.find_element_by_tag_name("body").send_keys(Keys.ESCAPE)
    browser.set_page_load_timeout(70)
    likes=browser.find_elements_by_xpath("//span[@class='_3t54']")
    for l1 in likes:
       
            
                l2= l1.find_element_by_xpath("//a[@class='_3emk _401_']")
                print l2.get_attribute('aria-label')

    browser.implicitly_wait(30)
    #browser.set_page_load_timeout(70)
  
    browser.find_element_by_tag_name("body").send_keys(Keys.ESCAPE)
    browser.implicitly_wait(30)
    

   
