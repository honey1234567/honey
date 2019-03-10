
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
ck="Jm6WDXZuiwlwUnT9mFbPdSpcg"
cs="Wp4Gbf74R6MZWjXvj0ifKrCobwWbchhn53Mv8L7VMLbIUi6Wnd"
at="919434545924935681-wFjVVTbs0pmyB2VwSoj4VwGb7tBYCyr"
ats ="RaPfxU0rSMjkS3MSI9N0ztXu4I2iLMecXg79OerNHw4Ly"


auth = OAuthHandler(ck, cs)
# set access token and secret
auth.set_access_token(at, ats)

# create tweepy API object to fetch tweets
api = tweepy.API(auth)
message="glad to see you on being a part of our organization.plz chech http://google.com  gor our reviews and rating and give your beedback by logging into http://halware.org "
browser = webdriver.Chrome("C:/Users/mihir/Desktop/chromedriver_win32/chromedriver.exe")
emails = re.findall(r"[a-z0-9/:\.\-+_]+\.[com,org,in,us,net,edu,me,io]+",message)
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
