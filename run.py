from selenium import webdriver

from selenium.webdriver.common.by import By

import time


 
print("ru: Загрузка Браузера... ")
print("en: Starting Browser... ")

choto = webdriver.Firefox()
# For Chrome/Для Хром или Яндекс Браузера: choto = webdriver.Chrome()
# For Safari/Для Сафари: choto = webdriver.Safari()



print("ru: Входим на аккаунт...")
print("en: Loggining... ")


choto.get("https://roblox.com/login")


nik = choto.find_element(By.ID, "login-username")
parol = choto.find_element(By.ID, "login-password")


nik.send_keys("") # Nickname/Никнейм
parol.send_keys("") # Password/Пароль



voiti = choto.find_element(By.ID, "login-button")



voiti.click()



time.sleep(10)


x = 7
y = 8


x += 3


while x >= y:
 f = open("ostalos.txt", "r+")
 prosm = int(f.read())
 print("ru: Подписка на айди... ")
 print("en: Following... ")
 choto.get(f"https://roblox.com/users/{prosm}")
 tritochki = choto.find_element(By.ID, "popover-link")
 tritochki.click()
 time.sleep(2)
 podpis = choto.find_element(By.ID, "profile-follow-user")
 podpis.click()
 time.sleep(2)
 af = str(prosm - 1)
 f.truncate(0)
 f.seek(0)
 f.write(af)
 print("ru: УСПЕШНО ПОДПИСАНО! ПЕРЕХОД НА АЙДИ: " + af )
 print("en: FOLLOWED! JUMPING TO ID: " + af )
 f.close()
 time.sleep(3)
