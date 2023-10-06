from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("ru: Загрузка Браузера... ")
print("en: Starting Browser... ")

browser = webdriver.Firefox()
# For Chrome: browser = webdriver.Chrome()
# For Safari: browser = webdriver.Safari()
# For Firefox: browser = webdriver.Firefox()

print("en: Loggining... ")
browser.get("https://roblox.com/login")
username = choto.find_element(By.ID, "login-username")
password = choto.find_element(By.ID, "login-password")

username.send_keys("") # Type Roblox Account Nickname here
password.send_keys("") # Type Roblox Account Password here

voiti = choto.find_element(By.ID, "login-button")
voiti.click()
time.sleep(10)
x = 7
y = 8
x += 3
while x >= y:
 f = open("id.txt", "r+")
 prosm = int(f.read())
 print("Following... ")
 browser.get(f"https://roblox.com/users/{prosm}")
 tritochki = browser.find_element(By.ID, "popover-link")
 tritochki.click()
 time.sleep(2)
 podpis = choto.find_element(By.ID, "profile-follow-user")
 podpis.click()
 time.sleep(2)
 af = str(prosm - 1)
 f.truncate(0)
 f.seek(0)
 f.write(af)
 print("FOLLOWED! JUMPING TO ID: " + af )
 f.close()
 time.sleep(3)
