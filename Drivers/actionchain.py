# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import time

###########MOUSE OVER ACTION############
# driver=webdriver.Chrome(executable_path=r"C:\Users\User\eclipse-workspace\chromedriver.exe")
# driver.get("https://www.amazon.in/")
#  
# ac=ActionChains(driver)
#  
# try_prime=driver.find_element_by_xpath("//a[contains(@id,'nav-link-prime')]")
# ac.move_to_element(try_prime).perform()
#  
# time.sleep(3)
#   
# clik_prime=driver.find_element_by_xpath("//a[@href='/prime?ref=in-pr-tryprime-unrec-multi-benefit']")
# clik_prime.click()
 
# driver.quit()
################## DRAG AND DROP###############
# driver.get("http://demo.guru99.com/test/drag_drop.html")
#  
# ac=ActionChains(driver)
#  
# drag_bank=driver.find_element_by_xpath("//li[@id='credit2']")
# drop_element=driver.find_element_by_xpath("(//li[@class='placeholder'])[1]")
# ac.drag_and_drop(drag_bank,drop_element).perform()
#  
# driver.quit()

############# HOLD AND RELEASE###########

# driver.get("http://demo.guru99.com/test/drag_drop.html")
#  
# ac=ActionChains(driver)
#  
# drag_bank=driver.find_element_by_xpath("//li[@id='credit2']")
# drop_element=driver.find_element_by_xpath("(//li[@class='placeholder'])[1]")
#  
# ac.click_and_hold(drag_bank).release(drop_element).perform()










