from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.select import Select
from email._header_value_parser import get_attribute
from ctypes.macholib import framework
driver=webdriver.Chrome(executable_path=r"C:\Users\User\eclipse-workspace\chromedriver.exe")

# driver.get("https://www.facebook.com/")
# time.sleep(3)
# btn=driver.find_element_by_xpath("(//a[@role='button'])[1]")
# btn.click()
# time.sleep(5)
# clk=driver.find_element_by_xpath("//select[@id='month']")
# s=Select(clk)
# s.select_by_index(4)

#######1
# driver.get("https://www.facebook.com/")
# btn=driver.find_element_by_xpath("(//a[@role='button'])[1]")
# btn.click()
# time.sleep(5)
# year=driver.find_element_by_xpath("//select[@id='year']")
# s=Select(year) 
# all=s.options
#   
# time.sleep(3)
# for i in range(0,len(all)):          ###################if we use any operantion we use range(normal for loop)
#     if i%2==0:
#         years=all[i]
#         even_years=years.text
#         print(even_years)
# driver.quit()

################2 #############select by attribute value & print by get attribute
# driver.get("http://demo.guru99.com/test/newtours/register.php")
# btn=driver.find_element_by_xpath("//select[@name='country']")
# s=Select(btn)
# All=s.options
# for a in All:
#     att_value=a.get_attribute("Value")
#     s.select_by_value(att_value)
#     data=btn.get_attribute("value")
#     print(data)
#####################3#######################Frame
###########by ID or nmame
# driver.get("http://demo.guru99.com/test/guru99home/")
# driver.switch_to.frame("a077aa5e")
# im=driver.find_element_by_xpath("//img[@src='Jmeter720.png']")
# im.click()

#############by webelement
# driver.get("http://demo.guru99.com/test/guru99home/")
# frame_path=driver.find_element_by_xpath("//iframe[@id='a077aa5e']")
# driver.switch_to.frame(frame_path)
# img=driver.find_element_by_xpath("//img[@src='Jmeter720.png']")
# img.click()

#################Index
# list_of=driver.find_element_by_tag_name("iframe")
# driver.switch_to.frame(2)