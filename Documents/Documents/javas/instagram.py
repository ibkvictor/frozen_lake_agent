import selenium
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib
import sys
import tensorflow
sys.path.append('/usr/local/bin')
import password

# driver = webdriver.Chrome()
# driver.get("http://www.google.com")
# element = driver.find_element_by_xpath("//div[2]/div[1]/div[1]/div/div[2]")
# inner_element = element.find_element_by_xpath("/input")
# inner_element.clear()
# element.send_keys('google')
# element.send_keys(Keys.RETURN)

class InstagramBot:


    def __init__(self, username):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def browser(self):
        url = "http://www.instagram.com/"
        self.driver.get(url)
        sleep(2)
        


    def shutdown(self):
        driver = self.driver
        driver.close()

    def login(self):
        driver = self.driver
        self.browser()
        driver.get("http://www.instagram.com/accounts/login/")
        # login_option = driver.find_element_by_xpath("//a[@href = '/accounts/login/']")
        # login_option.click()
        sleep(2)
        username_field = driver.find_element_by_xpath("//input[@name = 'username']")
        username_field.clear()
        username_field.send_keys(self.username)
        password_field = driver.find_element_by_xpath("//input[@name = 'password']")
        password_field.clear()
        password_field.send_keys(password.password_key.password)
        password_field.send_keys(Keys.RETURN)
        sleep(5)
        notification_request = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
        notification_request.click()
        sleep(2)

        # //a[@href = '/account/login/']
        # //button[@name = 'login']
        # //input[@name = 'username']
        # //input[@name = 'password']
    def like_photo(self, instagram_tag):
        driver = self.driver
        driver.get("http://www.instagram.com/"+ instagram_tag +"/")

        for i in range(1, 3):
            driver.execute_script("window.scrollTO(0, document.body.scrollheight)")
            sleep(1)

        things_to_like = driver.find_elements_by_tag_name('a')
        things_to_like_href =[elements.get_attribute('href') for elements in things_to_like]
        things_to_like_href = [elements for elements in things_to_like_href if instagram_tag in elements]
        #part of my work is to try if .contains() works

        for elements in things_to_like_href:
            try:
                liking_photo = driver.find_element_by_link_text('Like')
                liking_photo.click()
            except Exception as e:
                sleep(2)



    def getting(self):
        driver = self.driver
        wayout = self.username
        my_profile = driver.find_element_by_xpath("//a[contains(text(),'{}')]".format(self.username))
        my_profile.click()
        sleep(2)
        followers_show = driver.find_element_by_xpath("//a[contains(@href, '/followers')]")
        followers_show.click()
        sleep(2)
        followers_container = driver.find_element_by_xpath("//div[@class='isgrP']")
        driver.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight)', followers_container)
        sleep(2)
        lastheight, newheight = 0,1

        while lastheight != newheight:
            lastheight = newheight
            sleep(2)
            newheight = driver.execute_script("arguments[0].scrollTo(0,arguments[0].scrollHeight);return arguments[0].scrollHeight;",followers_container)
        
        counter = 0
        followers_list = []
        followers_list_link = followers_container.find_elements_by_xpath('//a')
        followers_list_link1 = [element for element in followers_list_link if str(element.get_attribute("class")) == 'FPmhX notranslate _0imsa ']
        print (len(followers_list_link))
        followers_list = [element.get_attribute('text()') for element in followers_list_link1]

        for e in followers_list:
            button_path2 ="//a[text() = '"+str(e)+"']/ancestor::div[@class = ' Igw0E rBNOH eGOV_ ybXk5 _4EzTm XfCBB HVWg4 ']//button[contains(text(), 'Follow')]"
            print (str(followers_list))
            sleep(3)
            polecien = driver.find_element_by_xpath(button_path2)
            polecien1 = polecien.get_attribute('text()')
            if str(polecien1) == "Follow":
                sleep(2)
                follow(e)
                print (str(e))
                # follow(e)
                counter += counter
                sleep[2]
            else:
                continue

    def follow(self, people):
        driver = self.driver
        clicking_follow = driver.find_element_by_xpath("//a[text() = '"+people+"']/ancestor::div[@class = ' Igw0E rBNOH eGOV_ ybXk5 _4EzTm XfCBB HVWg4 ']//button[contains(text(), 'Follow')]")
        clicking_follow.click()
    
    def story_viewing(self):
        driver = self.driver
        open_story = driver.find_element_by_xpath()
        open_story.click()
        sleep(2)
        close_story = driver.find_element_by_xpath()
        close_story.click()
    
    def chat_bot(self):
        pass

bot = InstagramBot("ibkvictor")
bot.login()
bot.getting()