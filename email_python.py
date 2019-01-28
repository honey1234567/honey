'''
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
from textblob import TextBlob #text/tweet parse
from itertools import permutations

#options='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@!#$%^&*'
#for w in permutations(options,8):
#        print w
ck="Jm6WDXZuiwlwUnT9mFbPdSpcg"
cs="Wp4Gbf74R6MZWjXvj0ifKrCobwWbchhn53Mv8L7VMLbIUi6Wnd"
at="919434545924935681-wFjVVTbs0pmyB2VwSoj4VwGb7tBYCyr"
ats ="RaPfxU0rSMjkS3MSI9N0ztXu4I2iLMecXg79OerNHw4Ly"


auth = OAuthHandler(ck, cs)
# set access token and secret
auth.set_access_token(at, ats)

# create tweepy API object to fetch tweets
api = tweepy.API(auth)

fr=[]
user=api.get_user('shreya73767208')

       
#api.send_direct_message('1053918664112500741L',text='message text here')    
#####################################################################################################################################################
browser = webdriver.Chrome("C:/Users/mihir/Desktop/chromedriver_win32/chromedriver.exe")
url = 'https://twitter.com/login?lang=en'
browser.get(url)
browser.implicitly_wait(30)


browser.find_element_by_class_name('js-username-field').send_keys('shreya73767208')
browser.find_element_by_class_name('js-password-field').send_keys('9643350692')
browser.find_element_by_css_selector('button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium').click()
        
       
                
browser.get('https://twitter.com/settings/account')
print browser.find_element_by_css_selector('input#user_email.email-input').get_attribute('value')
#print browser.find_element_by_css_selector('span.device_number_with_country_code').text
browser.find_element_by_css_selector('a#user-dropdown-toggle.btn.js-tooltip.settings.dropdown-toggle.js-dropdown-toggle').click()
#browser.find_element_by_css_selector('li#signout-button.js-signout-button').click()
               



'''
import smtplib
content="hello world"
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()#identify computer
mail.starttls()#transport layer security
mail.login('contact2theshreya@gmail.com','9643351461')
sender='contact2theshreya@gmail.com'
recipitent='bhaidon292@yahoo.com'
header='To:' + sender + '\n' + 'From:' \
        + recipitent + '\n' + 'subject : ALERT \n'
content=header+"Your Password Strength is Very weak which can be hacked easily so plaese make your password strong"
mail.sendmail(sender,recipitent,content)
print "sent"
mail.close()

#bhaidon292@yahoo.com
#abcABC@98
