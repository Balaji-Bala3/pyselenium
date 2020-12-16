from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome(executable_path=r"C:\Users\User\eclipse-workspace\chromedriver.exe")
ac=ActionChains(driver)
# driver.get("https://netbanking.hdfcbank.com/netbanking/?_ga=2.176378149.1819882415.1533883212-608727520.1532670997")
# time.sleep(5)
# btn=driver.find_element_by_xpath("//img[@src='/gif/continue_new1.gif?v=1']")
# btn.click()

##########
# driver.get(" https://netbanking.canarabank.in/entry/ENULogin.jsp")
# time.sleep(5)
# btn=driver.find_element_by_xpath("//input[@class='btn btn-default']")
# btn.click()
# time.sleep(5)
# alert=driver.switch_to_alert()
# alert.accept()
# ##############################
# driver.get("http://demo.guru99.com/test/guru99home/")
# driver.maximize_window()
# time.sleep(5)
# img=driver.find_element_by_xpath("//img[@src='Jmeter720.png']")
# img.click()
# driver.quit()
# ac.double_click(text).perform()
# ac.double_click(text).perform()