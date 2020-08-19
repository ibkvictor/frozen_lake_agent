import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



class search:
    def __init__(self):
        self.driver = webdriver.Chrome()

    data = []
    def get_data(self):
        driver = self.driver
        driver.get("http://www.google.com/")
        time.sleep(2)
        element = driver.find_element_by_xpath("//input[@type = 'text']")
        element_inner = element.find_element_by_xpath("//div[]")
        element_inner.clear()
        element_inner.send_keys('spinning mills in africa')
        element_inner.send_keys(Keys.RETURN)
        time.sleep(2)
        elementone = driver.find_element_by_xpath("//span[contains(text(), 'Union Spinning')]")
        elementone.click()
        time.sleep(1)
        elementtow = driver.find_elements_by_xpath("//a/div/div/div")
        
        elementtrrow = [elem for elem in elementtow]
        elementtrrow1 = [elem1.get_attribute('text()') for elem1 in elementtrrow]
        print (elementtrrow1)

google =  search()
google.get_data()