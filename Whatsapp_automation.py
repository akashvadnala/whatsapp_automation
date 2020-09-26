from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By



name = input("Enter name to whom you want to send message ")
name = name.split(',')
name = list(map(lambda x:x.strip(),name))
count = int(input("number of times to send same message "))
text = input("Enter your message ")

driver = webdriver.Chrome(r"C:\Users\91799\PycharmProjects\myprojects\chromedriver.exe")
                                #give the path of your chromedriver in your pc


def open_whataspp():
    print("Scan the QR code")
    driver.get("https://web.whatsapp.com/")


'''def send_message():
    try:
        user = WebDriverWait(driver, 60).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]')))
        user.send_keys("{}".format(name))
        user.send_keys(Keys.RETURN)
        message = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
        for i in range(count):
            message.send_keys(text)
            message.send_keys(Keys.RETURN)
        sleep(count*0.5)
    except:
        print('User not found. Exiting program')'''

def send_message():
    try:
        user = WebDriverWait(driver, 60).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]')))
        for i in name:
            user.send_keys("{}".format(i))
            user.send_keys(Keys.RETURN)
            message = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
            for j in range(count):
                message.send_keys(text)
                message.send_keys(Keys.RETURN)
        sleep(count*0.5)
    except:
        print('User not found. Exiting program')


def logout():
    # Click on options menu for log-out
    log = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]')
    log.click()
    out = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[6]/div')
    out.click()
    print('Logged out successfully')
    driver.quit()
    print('Connection was closed')

open_whataspp()
send_message()
logout()