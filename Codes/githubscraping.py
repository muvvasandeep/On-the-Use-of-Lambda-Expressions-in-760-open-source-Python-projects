from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from time import sleep
from getpass import getpass
import time
import sys
from selenium.webdriver.support import expected_conditions as EC
from collections import defaultdict as dd
dic=dd(list)
url = "https://github.com/login"
fsandeep=open("failure.txt",'a',encoding='utf-8')
repo = []
temp = []

repo_stars=dd(str)

def repo_name(link):
    x=''
    for i in range(len(link)-1,-1,-1):
        if link[i]=='/':
            break
        x+=link[i]
    print("ulta",x[::-1])
    return x[::-1]
        
def login(driver,usr,pwd):                          
    driver.get(url)
    print ("Opened github")
    sleep(1)
    username_box = driver.find_element_by_id('login_field')
    username_box.send_keys(usr)
    print ("Email Id entered")
    sleep(1)
    password_box = driver.find_element_by_id('password')
    password_box.send_keys(pwd)
    print ("Password entered")
    login_box = driver.find_element_by_class_name('btn-block')
    login_box.click()
    sleep(3)
def extract_repo(driver):
    reposit=driver.find_elements_by_class_name('v-align-middle')
    stars=driver.find_elements_by_xpath('//*[@id="js-pjax-container"]/div/div[3]/div/ul/li/div[2]/div[2]')
    temp_repo = []
    for i in range(0,len(reposit)):
        link=reposit[i].get_attribute('href')
        if link!=None:
            repo.append(reposit[i].get_attribute('href'))
            temp_repo.append(reposit[i].get_attribute('href'))
    print(len(temp_repo),len(stars))
    for i in range(0,len(temp_repo)):
        name=repo_name(temp_repo[i])
        repo_stars[name+'-master']=stars[i].text
        
    lang = driver.find_elements_by_xpath('//*[@id="js-pjax-container"]/div/div[3]/div/ul/li/div[2]/div[1]')
    stars=driver.find_elements_by_xpath('//*[@id="js-pjax-container"]/div/div[3]/div/ul/li/div[2]/div[2]')
    #print(len(lang))
    #print(len(stars))
    for i in range(0,len(lang)):
        pyt = lang[i].text
        #star=stars[i].text
        if pyt!=None:
            temp.append(pyt)
        
options = Options()
options.add_argument("--disable-notifications") 
driver = webdriver.Chrome(r"C:\Users\muvva\Documents\chromedriver.exe",chrome_options=options)
usr="shubham.rsangle@gmail.com"
pwd ="cs16b026"
login(driver,usr,pwd)
url='https://github.com/'
search="python"
num_pages=100
sear=search.split(' ')
search_url=''
for j in sear:
    search_url+=j+'+'
search_url=search_url[:-1]
print(search_url)

for z in range(0,1+num_pages):
    driver.get(url+'search?l=Python&o=desc&p='+str(z)+'&q=Python&s=stars&type=Repositories')
    #https://github.com/search?l=Python&o=desc&p=66&q=Python&s=stars&type=Repositories
    sleep(3)
    print("Item searched")
    extract_repo(driver)


for i in range(0,len(repo)):
    dic[temp[i]].append(repo[i])
python_repos = dic["Python"]

#driver.get('https://github.com/ansible/ansible/archive/master.zip')
'''
for i in range(0,len(python_repos)):
    try:
        print(python_repos[i])
        driver.get(python_repos[i]+'/archive/master.zip')
        if "404: Not Found" in driver.page_source:
            fsandeep.write(python_repos[i])
            driver.get(python_repos[i])
        sleep(5)

    except:
        
        continue
'''
fsandeep.close()
import json
with open('result.json', 'w') as fp:
    json.dump(repo_stars, fp)
    
