from selenium import webdriver
browser = webdriver.Chrome()

browser.get('https://techstepacademy.com/training-ground')


input2_css_locator = "input[id='ipt2']"
button4_xpath_locator = "//button[@id = 'b4']"
dropdown_element = "//select[@name='mySelect']"
dropdown_second_element = "//option[@value='second']"

#Assign elements
input2_element = browser.find_element_by_css_selector(input2_css_locator)
butn4_element = browser.find_element_by_xpath(button4_xpath_locator)
dropdown = browser.find_element_by_xpath(dropdown_element)
second_dropdown_element = browser.find_element_by_xpath(dropdown_second_element)

#Manipulate elements
input2_element.send_keys("Test text")
#butn4_element.click()
dropdown.location_once_scrolled_into_view
dropdown.click()
second_dropdown_element.click()


#browser.quit()


