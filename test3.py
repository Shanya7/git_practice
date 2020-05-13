from selenium import webdriver


browser1 = webdriver.Chrome()
browser2 = webdriver.Chrome()

browser1.get('http://techstepacademy.com/training-ground')
browser2.get('http://google.com/')
