from selenium import webdriver
browser = webdriver.Chrome()

browser.get("https://techstepacademy.com/trial-of-the-stones")

#Riddle 1
riddle1_input=browser.find_element_by_id('r1Input')
riddle1_answer_button= browser.find_element_by_id('r1Btn')
riddle1_result = browser.find_element_by_css_selector("div#passwordBanner> h4")

#Riddle 2
riddle2_input=browser.find_element_by_id('r2Input')
riddle2_answer_button= browser.find_element_by_id('r2Butn')


#Two Merchants
richest_merchant_name = browser.find_element_by_xpath("//p[text()='3000'] /../span")

#Riddle 3
riddle3_input = browser.find_element_by_id('r3Input')
riddle3_answer_button = browser.find_element_by_xpath("//button[@id='r3Butn']")

#Final check
check_answers=browser.find_element_by_css_selector("button[id='checkButn']")
check_result_total= browser.find_element_by_css_selector("div#trialCompleteBanner h4")

#Actions
riddle1_input.send_keys('rock')
riddle1_answer_button.click()
password = riddle1_result.text

riddle2_input.send_keys(password)
riddle2_answer_button.click()

rich= richest_merchant_name.text
riddle3_input.send_keys(rich)
riddle3_answer_button.click()

check_answers.click()
assert check_result_total.text == "Trial Complete"