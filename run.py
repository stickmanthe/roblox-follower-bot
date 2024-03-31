from selenium import webdriver
from selenium.webdriver.common.by import By
import time


putBrowser = input("Please enter the number to choose your browser (1 is Chrome, 2 is Safari, 3 is Firefox): ")
putUsername = input("Type your Roblox Account username here: ")
putPassword = input("Type Roblox Account Password here: ")

match putBrowser:
 case "1":
  print("Ok. Starting Chrome... ")
  browser = webdriver.Chrome()
 case "2":
  print("Ok. Starting Safari... ")
  browser = webdriver.Safari()
 case "3":
  print("Ok. Starting Firefox... ")
  browser = webdriver.Firefox()
 case _:
  print("Unknown browser!")
  exit()

print("Loggining in... ")
browser.get("https://roblox.com/login")
username = browser.find_element(By.ID, "login-username")
password = browser.find_element(By.ID, "login-password")

username.send_keys(putUsername)
password.send_keys(putPassword)

loginBtn = browser.find_element(By.ID, "login-button")
loginBtn.click()
time.sleep(10)

while True:
 f = open("id.txt", "r+")
 idRead = int(f.read())
 print("Following... ")
 browser.get(f"https://roblox.com/users/{idRead}")
 userOptions = browser.find_element(By.ID, "popover-link")
 userOptions.click()
 time.sleep(2)
 followUser = browser.find_element(By.LINK_TEXT, "Follow")
 followUser.click()
 time.sleep(2)
 af = str(idRead - 1)
 f.truncate(0)
 f.seek(0)
 f.write(af)
 print("FOLLOWED! JUMPING TO ID: " + af )
 f.close()
 time.sleep(3)
