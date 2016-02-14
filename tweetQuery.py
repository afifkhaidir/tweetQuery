import time,datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Open session to write
outputFile = open("output.csv", "w+")
outputFile.write('username;date;time;text;placeID\n')

#Open webdriver Chrome
#Use location to your chromedriver.exe
browser = webdriver.Chrome("C:/Users/Nurhikmah Afief/Documents/chromedriver.exe")

#search url
browser.get("https://twitter.com/search?q=%23prayforriau%20since%3A2015-01-01%20until%3A2015-10-01&src=typd")
time.sleep(1)

elem = browser.find_element_by_tag_name("body")

#Scroll value
scroll = 500

while scroll:
	elem.send_keys(Keys.PAGE_DOWN)
	time.sleep(0.2)
	scroll-=1
	
tweet_contents = browser.find_elements_by_css_selector("div > div.content")

for tweet in tweet_contents:
	#Tweet text
	text = tweet.find_element_by_css_selector("div.js-tweet-text-container > p").text.encode('ascii', 'ignore')
	
	#Username
	username = tweet.find_element_by_css_selector("div.stream-item-header > a > span.username.js-action-profile-name > b").text.encode('ascii', 'ignore')
	
	#Date of tweet
	dateInt = int(tweet.find_element_by_css_selector("div.stream-item-header > small > a > span").get_attribute('data-time'))
	dateFormat = datetime.datetime.fromtimestamp(dateInt)
	
	#Place ID
	if len(tweet.find_elements_by_class_name("Tweet-geo")) > 0:
		placeID = tweet.find_element_by_css_selector("div.stream-item-header > span > a").get_attribute('data-place-id')
	else:
		placeID = ''
	
	outputFile.write('%s;%s;%s;"%s";%s\n' % (username, dateFormat.strftime("%Y-%m-%d"),dateFormat.strftime("%H:%M"), text, placeID))