
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
import unittest, time, re
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import threading
import time
import tweepy
from tweepy import OAuthHandler
from tweepy import Cursor 
import re # regular expression
from textblob import TextBlob
def m():
    
ck="Jm6WDXZuiwlwUnT9mFbPdSpcg"
cs="Wp4Gbf74R6MZWjXvj0ifKrCobwWbchhn53Mv8L7VMLbIUi6Wnd"
at="919434545924935681-wFjVVTbs0pmyB2VwSoj4VwGb7tBYCyr"
ats ="RaPfxU0rSMjkS3MSI9N0ztXu4I2iLMecXg79OerNHw4Ly"


auth = OAuthHandler(ck, cs)
# set access token and secret
auth.set_access_token(at, ats)

# create tweepy API object to fetch tweets
api = tweepy.API(auth)
browser = webdriver.Chrome("C:/Users/mihir/Desktop/chromedriver_win32/chromedriver.exe")
#url='https://twitter.com/'
url = 'https://twitter.com/login?lang=en'
browser.get(url)
browser.find_element_by_class_name('js-username-field').send_keys('shreya73767208')
browser.find_element_by_class_name('js-password-field').send_keys('9643350692')
browser.find_element_by_css_selector('button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium').click()
browser.find_element_by_css_selector('span.Icon.Icon--dm.Icon--large').click()
word=browser.find_element_by_css_selector('p.DMInboxItem-snippet').text
text=word.split(":")
#print text
name=text[0]
print name
    
message=text[1]
print message
'''
emails = re.findall(r"[a-z0-9/:\.\-+_]+\.[a-z]+",message)
#print emails
for i in range(0,len(emails)):
    print emails[i]

url = 'https://validator.w3.org/checklink?uri=shreya.com&hide_type=all&depth=&check=Check'
browser.get(url)
#print browser.find_element_by_css_selector('p.DMInboxItem-snippet').text
for i in range(0,len(emails)):
    
        #browser.implicitly_wait(20) 
        browser.find_element_by_css_selector("input#uri_1").clear()
        browser.find_element_by_css_selector("input#uri_1").send_keys(emails[i])
        browser.find_element_by_css_selector("p.submit_button").click()


        try:
            element=browser.find_element_by_css_selector("div.intro")
            print emails[i],"is bad"
        except NoSuchElementException:
            print emails[i]," is good"
        #if browser.find_element_by_css_selector("div.intro").text:
            #print "error"
        #if browser.find_element_by_css_selector("div#progressresults1.progress"):
    #print "good"
#browser.find_element_by_css_selector("div.intro").text

#browser.find_element_by_css_selector('iron-icon#icon.style-scope.paper-icon-button.x-scope.iron-icon-0').click()

'''

