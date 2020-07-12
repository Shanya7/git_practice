from selenium import webdriver
browser = webdriver.Chrome()


browser.get('https://techstepacademy.com/iframe-training')

iframe = browser.find_element_by_css_selector("iframe")
browser.switch_to.frame(iframe)

paragraph_element = browser.find_element_by_css_selector("div[id = 'block-ec928cee802cf918d26c'] div p")