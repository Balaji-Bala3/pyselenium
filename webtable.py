# from selenium import webdriver
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import time
# from selenium.webdriver.support.select import Select
# from email._header_value_parser import get_attribute
# driver=webdriver.Chrome(executable_path=r"C:\Users\User\eclipse-workspace\chromedriver.exe")
# ac=ActionChains(driver)

# driver.get("https://www.w3schools.com/html/html_tables.asp")
#####################################################To get the table
# table=driver.find_element_by_id("customers")
####################################################To print all rows in table
# trows=driver.find_elements_by_tag_name("tr")
# print(type(trows))
# for i in range(0,len(trows)):
#     each_row=trows[i]
#     row_text=each_row.text
#     print(row_text)
# driver.quit()
###################################################To get particular row
# row=trows[2]
# r=row.text
# print(r)
####################################################to print all the headers in table:
# table=driver.find_element_by_id("customers")
# trows=table.find_elements_by_tag_name("tr")
# for i in range(0,len(trows)):
#     each_rows=trows[i]
#     theads=each_rows.find_elements_by_tag_name("th")
#     for each_head in theads:
#         head_text=each_head.text
#         print(head_text)
# driver.quit()

################################################### to get print all tr:
# table=driver.find_element_by_id("customers")
# trows=table.find_elements_by_tag_name("tr")
# for each_rows in trows:
#     text=each_rows.text
#     print(text)
################################################# to get print of particular data:
# table=driver.find_element_by_id("customers")
# trows=table.find_elements_by_tag_name("tr")
# for Each_rows in trows:                                 #####Enhanced for loop
#     tdata=Each_rows.find_elements_by_tag_name("td")
#     for rows in tdata:
#         data=rows.text
#         if data=="Canada":
#             print(data)
# driver.quit()
#################################################################ORRRRRRRR
# table=driver.find_element_by_id("customers")
# trows=table.find_elements_by_tag_name("tr")
# for i in range(0,len(trows)):
#     Each_rows=trows[i]                                 #####normal for loop
#     tdata=Each_rows.find_elements_by_tag_name("td")
#     for i in range(0,len(tdata)):
#         data=tdata[i]
#         raw_data=data.text
#         if raw_data=="Canada":
#             print(raw_data)
# driver.quit()
################# to get the particular data's row and column id:
# table=driver.find_element_by_id("customers")
# trows=table.find_elements_by_tag_name("tr")
# print(type(trows))
# for i in range(0,len(trows)):                    ##############Normal for loop
#     each_rows=trows[i]            ###################each_rows = webelement
# #     print(type(i))
# #     print(i)           ########################i = int
# #     print(type(each_rows))
# #     print(each_rows.text)
# # #     print(each_rows.text)
#     tdatas=each_rows.find_elements_by_tag_name("td")
#     for j in range(0,len(tdatas)):
#         each_data=tdatas[j]
#         data=each_data.text
#         if data=="Canada":
#             print(i)
#             print(j)
# driver.quit()
###################################################OR####################
# table=driver.find_element_by_id("customers")
# trows=table.find_elements_by_tag_name("tr")
# print(type(trows))
# for i in range(0,len(trows)):
#     each_rows=trows[i]
#     tdatas=each_rows.find_elements_by_tag_name("td")
#     for j in range(0,len(tdatas)):
#         each_data=tdatas[j].text
#         if each_data=="Canada":
#             print(i)
#             print(j)
# driver.quit()
#############################to print all the even rows in the table
# table=driver.find_element_by_id("customers")
# tdatas=table.find_elements_by_tag_name("tr")
# for i in range(0,len(tdatas)):
#     if i%2==0 and i!=0:
# #             print(i,type(i))
#         Each_data=tdatas[i]
#         data=Each_data.text
#         print(data)
# driver.quit()
################################to print all odd rows
# table=driver.find_element_by_id("customers")
# tdatas=table.find_elements_by_tag_name("tr")
# for i in range(0,len(tdatas)):
#     if i%2!=0 and i!=0:
# #             print(i,type(i))
#         Each_data=tdatas[i]
#         data=Each_data.text
#         print(data)
# driver.quit()
###############################to print all first three rows:
# table=driver.find_element_by_id("customers")
# tdatas=table.find_elements_by_tag_name("tr")
# for i in range(0,4):
#     if  i!=0:
# #             print(i,type(i))
#         Each_data=tdatas[i]
#         data=Each_data.text
#         print(data)
# driver.quit()
#################################to print last two rows
# table=driver.find_element_by_id("customers")
# tdatas=table.find_elements_by_tag_name("tr")
# for i in range(5,len(tdatas)):
#     if  i!=0:
#         Each_data=tdatas[i]
#         data=Each_data.text
#         print(data)
# driver.quit()
##################################to alternative
# table=driver.find_element_by_id("customers")
# tdatas=table.find_elements_by_tag_name("tr")
# for i in range(0,len(tdatas),2):
#     if  i!=0:
#         Each_data=tdatas[i]
#         data=Each_data.text
#         print(data)
# driver.quit()
############################# to print middle row
# table=driver.find_element_by_id("customers")
# tdatas=table.find_elements_by_tag_name("tr")
# for each_rows in tdatas:
#     middle=int(len(tdatas)//2)
#     text=(tdatas[middle])
# data=text.text
# print(data)



















