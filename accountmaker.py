from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import randint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select

def makepassword():
    l = ["a", "b", "c", "d", "e","f","x", "q", "z", "y", "k"]
    strn = ""
    for i in range(20):
        strn += l[randint(0, len(l)-1)]
    return strn

def makeemail(strf, strl):
    strn = strf.strip()+strl.strip()
    l = ["a", "b", "c", "d", "e","f","x", "q", "z", "y", "k"]
    for i in range(10):
        strn += l[randint(0, len(l)-1)]
    return strn + "@gmail.com"

first = input()
last = input()
email = makeemail(first, last)
password = makepassword()
f = email+".txt"
df= open(f,"w+")
df.write(first)
df.write(" ")
df.write(last)
df.write(" ")
df.write(email)
df.write(" ")
df.write(password)
df.write(" ")
df.close()
browser = webdriver.Chrome('/Users/vikramiyer/Documents/chromedriver')
browser.get('https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp')
inputElement = browser.find_element_by_id("firstName")
inputElement.send_keys(first)
inputElement = browser.find_element_by_id("lastName")
inputElement.send_keys(last)
inputElement = browser.find_element_by_id("username")
inputElement.send_keys(email)
inputElement = browser.find_element_by_name("Passwd")
inputElement.send_keys(password)
inputElement = browser.find_element_by_name("ConfirmPasswd")
inputElement.send_keys(password)
browser.find_element_by_css_selector('#accountDetailsNext').click()
time.sleep(3)
inputElement = browser.find_element_by_id("phoneNumberId")
inputElement.send_keys('510-402-3579')
browser.find_element_by_xpath("//*[@id=\"gradsIdvPhoneNext\"]").click()
WebDriverWait(browser, 15).until(EC.url_changes(browser.current_url))
time.sleep(10)
select = Select(browser.find_element_by_id('month'))
select.select_by_value(str(randint(1,12)))
inputElement = browser.find_element_by_id("day")
inputElement.send_keys(str(randint(1,30)))
inputElement = browser.find_element_by_id("year")
inputElement.send_keys(str(randint(1973, 2004)))
