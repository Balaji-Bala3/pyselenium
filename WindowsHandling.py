from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.select import Select
from email._header_value_parser import get_attribute
import keyboard
# from keyboard import keys 
# from keyboard import press
from keyboard import *
import keyword
driver=webdriver.Chrome(executable_path=r"C:\Users\User\eclipse-workspace\chromedriver.exe")
ac=ActionChains(driver)
##############1
# driver.get("https://www.amazon.com/")
# driver.maximize_window()
# search_bar=driver.find_element_by_id("twotabsearchtextbox")
# search_bar.send_keys("iPhone X")
# time.sleep(3)
# search_btn=driver.find_element_by_xpath("(//input[@class='nav-input'])[2]")
# search_btn.click()
# phone=driver.find_element_by_xpath("//img[@alt='iPhone X']")
# ac.context_click(phone).perform()
# keyboard.press("down arrow")
# keyboard.release("down arrow")
# keyboard.press("Enter")
#####################2
# driver.get("https://www.snapdeal.com/")
# driver.maximize_window()
# time.sleep(3)
# search_bar=driver.find_element_by_xpath("//input[@class='col-xs-20 searchformInput keyword']")
# search_bar.send_keys("iphone 7 pro mobile phone")
# time.sleep(3)
# search_btn=driver.find_element_by_xpath("//span[@class='searchTextSpan']")
# search_btn.click()
# time.sleep(2)
# img=driver.find_element_by_xpath("(//img[@class='product-image '])[1]")
# img.click()
# ##### to get all windows id
# All_id=driver.window_handles
# print(All_id)
# ########### switch to window
# time.sleep(3)
# Window2=driver.switch_to.window(All_id[1])
# time.sleep(3)
# add_cart=driver.find_element_by_id("add-cart-button-id")
# add_cart.click()