from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)
driver.get('https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=005&aid=0001333549')
title = driver.find_element_by_id('articleTitle')
body = driver.find_element_by_id('articleBodyContents')
print(title.text)
print(body.text)