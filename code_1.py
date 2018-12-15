#Husain Shaikh
import selenium.webdriver as webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("This program traverses the wikipedia website until it reaches the Language page.")
traversed=[]

start=input("Please enter a search term to start with : ")
title=""
url="https://en.wikipedia.org/wiki/"
surl=url+start

browser=webdriver.Safari()
browser.get(surl)
title=WebDriverWait(browser,2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/h1')))
traversed.append(title.text)
title=title.text
flag=0
if(title=="language" or title=="Language"):
	flag=1
count=0
while(not (title=="language" or title=="Language" or flag==1)):
	new_url=WebDriverWait(browser,2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mw-content-text"]/div/p/a')))
	count+=1
	title=str(new_url.text)
	new_url=WebDriverWait(browser,2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mw-content-text"]/div/p/a'))).click()
	if(title in traversed):
		flag=0
		print("It makes a loop!")
		traversed.append(title)
		break
	traversed.append(str(title))
	print(title)
	time.sleep(3)
	
browser.close()

if("language" in traversed or "Language" in traversed):
	flag=1

if(flag==1):
	print("We found the page in {} iterations.".format(count))
else:
	print("We could not find the page!")
print(str(traversed))
