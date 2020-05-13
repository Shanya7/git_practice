from selenium import webdriver
browser = webdriver.Chrome()

browser.get('http://techstepacademy.com/training-ground')

browser.execute_script('window.open("http://techstepacademy.com/training-ground", "_blank");')
browser.execute_script('window.open("http://google.com", "_blank");')
browser.execute_script('window.open("http://amazom.com", "_blank");')
browser.execute_script('window.open("http://ebay.com", "_blank");')
