from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# THIS PROJECT IS FAILED !

import time

path = "chromedriver.exe"

username = "usernamehere"
password = "passwordhere"

def separate_number(getmessage):
    a = getmessage.split(" ")
    return int(a[1])

def get_follower_list(driver, count):
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
    time.sleep(3)
    mylist = []
    i = 0
    while i <= count:
        i += 1
        mylist.append(driver.find_element_by_xpath(f"/html/body/div[6]/div/div/div[2]/ul/div/li[{i}]/div/div[1]/div[2]/div[1]/span/a").text)
    driver.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/div/div[2]/button/div/svg").click()
    time.sleep(1)
    return mylist

def get_following_list(driver, count):
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
    time.sleep(3)
    mylist = []
    i = 0
    while i <= count:
        i += 1
        mylist.append(driver.find_element_by_xpath(f"/html/body/div[6]/div/div/div[3]/ul/div/li[{i}]/div/div[2]/div[1]/div/div/span/a").text)
    driver.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/div/div[2]/button/div/svg").click()
    time.sleep(1)
    return mylist

def extract_number(followerlist, followinglist):
    extractionlist = []
    for i in followinglist:
        if i not in followerlist:
            extractionlist.append(i)
    return extractionlist

webdriver_options = webdriver.ChromeOptions()
#webdriver_options .add_argument('headless')

driver = webdriver.Chrome(path)

driver.get("https://www.instagram.com")

time.sleep(2)

driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()

time.sleep(2)

print("="*40)

print("로그인 완료\n")

driver.get(f"https://www.instagram.com/{username}")

print("프로필 사이트 로딩 완료")

time.sleep(3)

#get followers first
follower = separate_number(driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').text)
following = separate_number(driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').text)

print(f"팔로워 수: {follower}명, 팔로잉 수: {following}명")

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
time.sleep(3)

i = 1
while i <= follower:
    try:
        print(driver.find_element_by_xpath(f"/html/body/div[6]/div/div/div[2]/ul/div/li[{i}]/div/div[2]/div[1]/div/div/span/a").text)
    except:
        time.sleep(2)
        print(driver.find_element_by_xpath(f"/html/body/div[6]/div/div/div[2]/ul/div/li[{i}]/div/div[2]/div[1]/div/div/span/a").text)
    i += 1
    
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
time.sleep(3)
followerlist = []
i = 0
while i <= follower:
    i += 1
    followerlist.append(driver.find_element_by_xpath(f"/html/body/div[6]/div/div/div[2]/ul/div/li[{i}]/div/div[1]/div[2]/div[1]/span/a").text)
driver.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/div/div[2]/button/div/svg").click()
time.sleep(1)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
time.sleep(3)
followinglist = []
i = 0
while i <= following:
    i += 1
    followinglist.append(driver.find_element_by_xpath(f"/html/body/div[6]/div/div/div[3]/ul/div/li[{i}]/div/div[2]/div[1]/div/div/span/a").text)
driver.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/div/div[2]/button/div/svg").click()
time.sleep(1)

print(f"모든 팔로워/팔로잉 로딩 완료 | 대조하는 중")

with open("results.txt", "w") as f:
    f.write(extract_number(followerlist, followinglist))
    f.close()


print("완료")
print("="*40)

#팔로워 177
#/html/body/div[6]/div/div/div[2]/ul/div/li[1]/div/div[1]/div[2]/div[1]/span/a
#/html/body/div[6]/div/div/div[2]/ul/div/li[2]/div/div[1]/div[2]/div[1]/span/a
#/html/body/div[6]/div/div/div[2]/ul/div/li[177]/div/div[1]/div[2]/div[1]/span/a

#팔로우 148
#/html/body/div[6]/div/div/div[3]/ul/div/li[1]/div/div[2]/div[1]/div/div/span/a
#/html/body/div[6]/div/div/div[3]/ul/div/li[2]/div/div[2]/div[1]/div/div/span/a

#/html/body/div[6]/div/div/div[2]/ul/div/li[1]/div/div[2]/div[1]/div/div/span/a