from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Form:

#Constructor
   def __init__(self, url):
       self.url = url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       # Explicit wait
       self.wait = WebDriverWait(self.driver, 50)
#Boot Function

   def boot(self):
       self.driver.get(self.url)
       self.driver.maximize_window()
       self.wait.until(ec.url_to_be(self.url))


   def quit(self):
       self.driver.quit()
#Function to fill form
   def fillForm(self):
       self.boot()
       self.driver.execute_script('window.scrollBy(0, 800)')
       expandall=self.driver.find_element(By.XPATH,'//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/div/button/span')
       self.driver.execute_script("arguments[0].click();", expandall)
       self.wait.until(ec.presence_of_element_located((By.ID, "text-input__3"))).send_keys("Nivi")
       self.wait.until(ec.presence_of_element_located((By.ID, "text-input__8"))).send_keys("08-09-1992")
       self.driver.execute_script('window.scrollBy(0, 800)')
       self.wait.until(ec.presence_of_element_located((By.ID, "text-input__4"))).send_keys("09-1992")
       self.driver.execute_script('window.scrollBy(800, 0)')
       #variable declaration to search results
       results= self.driver.find_element(By.CLASS_NAME,'ipc-btn__text')
       self.driver.execute_script("arguments[0].click();", results)
       self.quit()




obj = Form("https://www.imdb.com/search/name/")
obj.fillForm()

